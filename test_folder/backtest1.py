import pandas as pd
import numpy as np
from datetime import datetime

def to_drawdown_series(prices):
    """
    Calculates the drawdown series.
    This returns a series representing a drawdown.
    When the price is at all time highs, the drawdown
    is 0. However, when prices are below high water marks,
    the drawdown series = current / hwm - 1
    The max drawdown can be obtained by simply calling .min()
    on the result (since the drawdown series is negative)
    Method ignores all gaps of NaN's in the price series.
    Args:
        * prices (Series or DataFrame): Series of prices.
    """
    # make a copy so that we don't modify original data
    drawdown = prices.copy()

    # Fill NaN's with previous values
    drawdown = drawdown.fillna(method='ffill')

    # Ignore problems with NaN's in the beginning
    drawdown[np.isnan(drawdown)] = -np.Inf

    # Rolling maximum
    roll_max = np.maximum.accumulate(drawdown)
    drawdown = drawdown / roll_max - 1.
    return drawdown


def calc_max_drawdown(prices):
    """
    Calculates the max drawdown of a price series. If you want the
    actual drawdown series, please use to_drawdown_series.
    """
    return (prices / prices.expanding(min_periods=1).max()).min() - 1


def drawdown_details(drawdown, index_type=pd.DatetimeIndex):
    """
    Returns a data frame with start, end, days (duration) and
    drawdown for each drawdown in a drawdown series.
    .. note::
        days are actual calendar days, not trading days
    Args:
        * drawdown (pandas.Series): A drawdown Series
            (can be obtained w/ drawdown(prices).
    Returns:
        * pandas.DataFrame -- A data frame with the following
            columns: start, end, days, drawdown.
    """

    is_zero = drawdown == 0
    # find start dates (first day where dd is non-zero after a zero)
    start = ~is_zero & is_zero.shift(1)
    start = list(start[start == True].index)  # NOQA

    # find end dates (first day where dd is 0 after non-zero)
    end = is_zero & (~is_zero).shift(1)
    end = list(end[end == True].index)  # NOQA

    if len(start) is 0:
        return None

    # drawdown has no end (end period in dd)
    if len(end) is 0:
        end.append(drawdown.index[-1])

    # if the first drawdown start is larger than the first drawdown end it
    # means the drawdown series begins in a drawdown and therefore we must add
    # the first index to the start series
    if start[0] > end[0]:
        start.insert(0, drawdown.index[0])

    # if the last start is greater than the end then we must add the last index
    # to the end series since the drawdown series must finish with a drawdown
    if start[-1] > end[-1]:
        end.append(drawdown.index[-1])

    result = pd.DataFrame(
        columns=('Start', 'End', 'Length', 'drawdown'),
        index=range(0, len(start))
    )

    for i in range(0, len(start)):
        dd = drawdown[start[i]:end[i]].min()

        if index_type is pd.DatetimeIndex:
            result.iloc[i] = (start[i], end[i], (end[i] - start[i]).days, dd)
        else:
            result.iloc[i] = (start[i], end[i], (end[i] - start[i]), dd)

    return result

# 計算 MaxDD
def DrawDownAnalysis(cumRet):
    dd_series = to_drawdown_series(cumRet)
    dd_details = drawdown_details(dd_series)
    return dd_details['drawdown'].min(), dd_details['Length'].max()

# 利用策略產生的持有部位資訊，計算底下四個指標來判斷投資績效
# sharpe ratio: 判斷報酬的好壞跟穩定度，數值越大越好
# maxdd: maximum drawdown, 最糟糕的狀況會賠幾 %
# maxddd: maximum drawdown duration, 低於上一次最高報酬的天數
# cumRet[-1]: 最後賺的 % 數
def indicators(df):
    dailyRet = df['Close'].pct_change()
    excessRet = (dailyRet - 0.04/252)[df['positions'] == 1]
    SharpeRatio = np.sqrt(252.0)*np.mean(excessRet)/np.std(excessRet)
    df['Ret'] = np.where(df['positions']==1, dailyRet, 0)
    cumRet = np.cumprod(1+df['Ret'])
    maxdd, maxddd = DrawDownAnalysis(cumRet)
    return np.round(SharpeRatio, 2), np.round(maxdd, 2), np.round(maxddd, 2), np.round(cumRet[-1], 2)

if __name__=="__main__":
    from crawler import get_quotes
    df = get_quotes('2330.tw', datetime(2017, 1, 1))
    df['positions'] = 1
    print(indicators(df))