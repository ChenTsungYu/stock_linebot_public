import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from crawler import get_quotes
import backtest
from matplotlib.font_manager import FontProperties # 設定字體
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')
# 讀取從指定日期之後的股價資訊
df = get_quotes("AAPL", datetime(2018,8,1))

# 突破策略
def breakout(df):
    # Donchian Channel
    df['20d_high'] = pd.Series.rolling(df['Close'], window=20).max()
    df['10d_low'] = pd.Series.rolling(df['Close'], window=10).min()

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

    # 底下這一行只是為了要在下面把 signals 跟 positions 畫出來做說明用
    df[['signals', 'positions']].plot(subplots = True, ylim=(-1.1, 1.1), figsize = (10, 8))
    # plt.savefig('break.png')

# 黃金交叉策略
def macross(df):
    # 均線
    df['20d'] = pd.Series.rolling(df['Close'], window=20).mean()
    df['5d'] = pd.Series.rolling(df['Close'], window=5).mean()

    has_position = False
    df['signals'] = 0
    for t in range(2, df['signals'].size):
        if df['5d'][t] > df['20d'][t] and df['5d'][t-1] < df['20d'][t-1] and df['20d'][t] > df['20d'][t-1]:
            if not has_position:
                df.loc[df.index[t], 'signals'] = 1
                has_position = True
        elif df['Close'][t] < df['20d'][t] and df['Close'][t-1] < df['20d'][t-1]:
            if has_position:
                df.loc[df.index[t], 'signals'] = -1
                has_position = False

    df['positions'] = df['signals'].cumsum().shift()

    # 底下這一行只是為了要在下面把 signals 跟 positions 畫出來做說明用
    df[['signals', 'positions']].plot(subplots = True, ylim=(-1.1, 1.1), figsize = (10, 8))
    # plt.savefig('cross.png')

def apply_strategy(strategy, df):
    return strategy(df)
apply_strategy(macross, df)
# fig = plt.figure()
# #fig.patch.set_facecolor('white')     # Set the outer colour to white
# ax1 = fig.add_subplot(111,  ylabel='Price in $')
    
# df['Close'].plot(ax=ax1, color='gray', lw=1., figsize=(10,8))
# # df['20d_high'].plot(ax=ax1, color='r', lw=1.)
# # df['10d_low'].plot(ax=ax1, color='b', lw=1.)
# df['5d'].plot(ax=ax1, color='r', lw=1.)
# df['20d'].plot(ax=ax1, color='b', lw=1.)

# # Plot the "buy" trades
# ax1.plot(df.loc[df.signals == 1].index,df['Close'][df.signals == 1],'^', markersize=10, color='r')

# # Plot the "sell" trades
# ax1.plot(df.loc[df.signals == -1].index, df['Close'][df.signals == -1], 'v', markersize=10, color='k')
# plt.savefig('trade.png')


# 計算Sharpe Ratio
dailyRet = df['Close'].pct_change()
#假設無風險利率為 4%
#假設一年有252個交易日
excessRet = (dailyRet - 0.04/252)[df['positions']==1]
df['Ret'] = np.where(df['positions']==1, dailyRet, 0)

# sharpeRatio = np.sqrt(252.0)*np.mean(excessRet)/np.std(excessRet)
# print(sharpeRatio)

# 計算MaxDD跟MaxDDD
# cumRet = np.cumprod(1 + df['Ret'])
# cumRet.plot(style='r-')
# plt.savefig('MaxDD.png')