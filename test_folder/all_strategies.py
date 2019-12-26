import numpy as np
import pandas as pd


def Breakout(df):
    """
    進場點：突破前一日的 20 日高點
    出場點：突破前一日的 10 日低點
    """
    # Donchian Channel
    df['20d_high'] = np.round(pd.Series.rolling(df['Close'], window=20).max(), 2)
    df['10d_low'] = np.round(pd.Series.rolling(df['Close'], window=10).min(), 2)

    has_position = False
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if df['Close'][t] > df['20d_high'][t-1]:
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif df['Close'][t] < df['10d_low'][t-1]:
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()
    return df


def BBand(df):
    """
    主要使用BBand + 5MA策略，
    中軌為20ma，上下軌為正負1.5sd
    # 若5MA開始向上突破下軌，低檔買進
    # 若收盤價向下跌破中軌，獲利了結趕快落跑
    """

    df['5ma'] = pd.Series.rolling(df['Close'], window=5).mean()
    # bbands策略,N=20
    df['20ma'] = pd.Series.rolling(df['Close'], window=20).mean()
    df['SD'] = pd.Series.rolling(df['Close'], window=20).std()
    # 上軌=20ma+1.5sd ,中軌=20ma, 下軌=20ma-1.5sd
    df['upbbands'] = df['20ma']+1.5*df['SD']
    df['midbbands']=df['20ma']
    df['lowbbands'] = df['20ma']-1.5*df['SD']

    has_position = False
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if  (df['5ma'][t] > df['lowbbands'][t-1]):
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif  (df['Close'][t] < df['midbbands'][t-1]):
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()
    return df


def WMSR(df):
    """
    WMSR < 80時進場
    WMSR > 20時出場
    """
    df['low9'] = df['Low'].rolling(window=9).min()
    df['high9'] = df['High'].rolling(window=9).max()
    df['WMSR'] = 100*((df['high9'] - df['Close']) / (df['high9'] - df['low9']) )

    has_position = False
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if df['WMSR'][t] < 80:
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif df['WMSR'][t] > 20:
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()
    return df


def BIAS(df):
    """
    乖離率,乖離率代表的就是投資者的平均報酬率，當股價漲離平均成本很多的時候，
    就可能會有大的獲利賣壓出現，讓股價往均線跌回,當股價跌出平均成本太多的時候，攤平或逢低的買盤可能會進入
    乖離率<-3% 進場 , >3.5% 出場
    """
    has_position = False
    df['6d'] = pd.Series.rolling(df['Close'], window=6).mean()
    df['BIAS'] = (df['Close'] - df['6d'] )/df['6d']
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if df['BIAS'][t] < -0.03:
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif df['BIAS'][t] > 0.03:
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()
    return df


def MACD(df):
    """
     MACD：對長期與短期的移動平均線 收斂或發散的徵兆，加以雙重平滑處理，用來判斷買賣股票的時機與訊號(確定波段漲幅 找到買賣點)
     MACD策略：快線 (DIF) 向上突破 慢線 (MACD)。 → 買進訊號
               快線 (DIF) 向下跌破 慢線 (MACD)。→ 賣出訊號
    """
    df['EMAfast'] = pd.Series.ewm(df['Close'], span = 12).mean()
    df['EMAslow'] = pd.Series.ewm(df['Close'], span = 26).mean()
    df['DIF'] = (df['EMAfast'] - df['EMAslow'])
    df['MACD'] = pd.Series.ewm(df['DIF'], span = 9).mean()

    has_position = False
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if df['DIF'][t-1]<df['MACD'][t] and df['DIF'][t]>df['MACD'][t]:
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif df['DIF'][t-1]>df['MACD'][t] and df['DIF'][t]<df['MACD'][t]:
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()
    return df