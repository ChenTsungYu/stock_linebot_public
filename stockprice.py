# -*- coding: utf-8 -*-
''' 
即時股價
'''
import requests
import datetime
import json
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from bs4 import BeautifulSoup
import Imgur
from matplotlib.font_manager import FontProperties # 設定字體
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

emoji_upinfo = u'\U0001F447'
emoji_midinfo = u'\U0001F538'
emoji_downinfo = u'\U0001F60A'

def get_stock_name(stockNumber):
    try:
        url = f'https://tw.stock.yahoo.com/q/q?s={stockNumber}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find_all(text='成交')[0].parent.parent.parent
        stock_name = table.select('tr')[1].select('td')[0].text.strip('加到投資組合')
        return stock_name
    except:
        return "no"

# 使用者查詢股票
def getprice(stockNumber, msg):
    stock_name = get_stock_name(stockNumber)
    if stock_name == "no": return "股票代碼錯誤!"
    content = ""
    stock = pdr.DataReader(stockNumber+'.TW', 'yahoo',  end=datetime.datetime.now())
    date = stock.index[-1]
    price = '%.2f ' % stock["Close"][-1] # 近日之收盤價
    last_price = '%.2f ' % stock["Close"][-2] # 前一日之收盤價
    spread_price = '%.2f ' % (float(price) - float(last_price)) # 價差
    spread_ratio = '%.2f ' % (float(spread_price) / float(last_price)) # 漲跌幅
    spread_price = spread_price.replace("-",'▽ ') if last_price > price else '△ ' + spread_price
    spread_ratio = spread_ratio.replace("-",'▽ ') if  last_price > price else '△ ' + spread_ratio
    open_price = str('%.2f ' % stock["Open"][-1]) # 近日之開盤價
    high_price = str('%.2f ' % stock["High"][-1])# 近日之盤中高點
    low_price = str('%.2f ' % stock["Low"][-1]) # 近日之盤中低點
    price_five = stock.tail(5)["Close"] # 近五日之收盤價
    stockAverage = str('%.2f ' % pd.to_numeric(price_five).mean())  # 計算近五日平均價格
    stockSTD = str('%.2f ' % pd.to_numeric(price_five).std())   # 計算近五日標準差  
    content += f"回報編號{stock_name}的股價{emoji_upinfo}\n--------------\n日期: {date}\n{emoji_midinfo}最新收盤價: {price}\n{emoji_midinfo}開盤價{open_price}\n{emoji_midinfo}最高價: \
    {high_price}\n{emoji_midinfo}最低價: {low_price}\n{emoji_midinfo}價差: {spread_price} 漲跌幅: {spread_ratio}\n{emoji_midinfo}近五日平均價格: {stockAverage}\n{emoji_midinfo}近五日標準差: {stockSTD}\n"
    if msg[0] == "#": content += f"--------------\n需要更詳細的資訊，可以點選以下選項進一步查詢唷{emoji_downinfo}"
    else: content += '\n' 
    return content

# --------- 畫近一年股價走勢圖
def stock_trend(stockNumber, msg):
    stock_name = get_stock_name(stockNumber)
    end = datetime.datetime.now()
    date = end.strftime("%Y%m%d")
    year = str(int(date[0:4]) - 1)
    month = date[4:6]
    stock = pdr.DataReader(stockNumber+'.TW', 'yahoo', start= year+"-"+month,end=end)
    plt.figure(figsize=(12, 6))
    plt.plot(stock["Close"], '-' , label="收盤價")
    plt.plot(stock["High"], '-' , label="最高價")
    plt.plot(stock["Low"], '-' , label="最低價")
    plt.title(stock_name + '  收盤價年走勢',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.ylabel('價格', fontsize=20, fontproperties=font_path)
    plt.grid(True, axis='y') # 網格線
    plt.legend(fontsize=14, prop=font_path)
    plt.savefig(msg + '.png') #存檔
    plt.show()
    plt.close() 
    return Imgur.showImgur(msg)

#股票收益率: 代表股票在一天交易中的價值變化百分比
def show_return(stockNumber, msg):
    stock_name = get_stock_name(stockNumber)
    end = datetime.datetime.now()
    date = end.strftime("%Y%m%d")
    year = str(int(date[0:4]) - 1)
    month = date[4:6]
    stock = pdr.DataReader(stockNumber + '.TW', 'yahoo', start= year+"-"+month,end=end)
    stock['Returns'] = stock['Close'].pct_change()
    stock_return = stock['Returns'].dropna()
    plt.figure(figsize=(12, 6))
    plt.plot(stock_return, label="報酬率")
    plt.title(stock_name + '  年收益率走勢',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.ylabel('報酬率', fontsize=20, fontproperties=font_path)
    plt.grid(True, axis='y') # 網格線
    plt.legend(fontsize=14, prop=font_path)
    plt.savefig(msg+'.png') #存檔
    plt.show()
    return Imgur.showImgur(msg)

# --------- 畫  股價震盪圖
def show_fluctuation(stockNumber, msg):
    stock_name = get_stock_name(stockNumber)
    end = datetime.datetime.now()
    date = end.strftime("%Y%m%d")
    year = str(int(date[0:4]) - 1)
    month = date[4:6]
    stock = pdr.DataReader(stockNumber + '.TW', 'yahoo', start= year+"-"+month,end=end)
    stock['stock_fluctuation'] = stock["High"] - stock["Low"]
    max_value = max(stock['stock_fluctuation'][:]) # 最大價差
    min_value = min(stock['stock_fluctuation'][:]) # 最小價差
    plt.figure(figsize=(12, 6))
    plt.plot(stock['stock_fluctuation'], '-' , label="波動度", color="orange")
    plt.title(stock_name + '  收盤價年波動度',loc='center', fontsize=20, fontproperties=font_path)# loc->title的位置
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.ylabel('價格', fontsize=20, fontproperties=font_path)
    plt.grid(True, axis='y') # 網格線
    plt.legend(fontsize=14, prop= font_path)
    plt.savefig(msg + '.png') #存檔
    plt.show()
    plt.close() 
    return Imgur.showImgur(msg)
