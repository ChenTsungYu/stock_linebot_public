'''
策略優化
教學網址:
https://www.finlab.tw/Python%E6%96%B0%E6%89%8B%E6%95%99%E5%AD%B8%EF%BC%9A%E7%AD%96%E7%95%A5%E5%84%AA%E5%8C%96/

此檔可用，還在如何用在腳本上
'''
import io
import requests
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('ggplot')
from matplotlib.font_manager import FontProperties # 設定字體
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

def crawl_price(stock_id):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"

    response = requests.post(url)

    f = io.StringIO(response.text)
    df = pd.read_csv(f, index_col='Date', parse_dates=['Date'] )
    return df


twii = crawl_price("^TWII") #台股大盤資料
# print(twii.head())
mean = twii['Adj Close'].pct_change().rolling(252).mean()
std = twii['Adj Close'].pct_change().rolling(252).std()

sharpe = mean / std

# twii.Close.plot()
# sharpe.plot(secondary_y=True)
# plt.savefig('test.png')

# sharpe ratio 平滑
sr = sharpe
srsma = sr.rolling(60).mean()

# sharpe ratio 的斜率
srsmadiff = srsma.diff()

# 計算買入賣出點
buy = (srsmadiff > 0) & (srsmadiff.shift() < 0)
sell = (srsmadiff < 0) & (srsmadiff.shift() > 0)

# 計算持有時間
hold = pd.Series(np.nan, index=buy.index)
hold[buy] = 1
hold[sell] = 0
hold.ffill(inplace=True)
hold.plot()

# 持有時候的績效
adj = twii['Adj Close'][buy.index]
(adj.pct_change().shift(-1)+1).fillna(1)[hold == 1].cumprod().plot()
plt.savefig('test1.png')

