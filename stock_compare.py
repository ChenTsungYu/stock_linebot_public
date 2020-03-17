'''
Created by Tsung Yu on 17/03/2020.
Copyright © 2020 Tsung Yu. All rights reserved.

用於比較兩檔以上股票的走勢 
參考相關文章
https://ithelp.ithome.com.tw/articles/10205113?source=post_page-----d9ef82dc4175----------------------
https://ithelp.ithome.com.tw/articles/10205068

https://www.jianshu.com/p/b22bd9a587a2

'''
import requests
from bs4 import BeautifulSoup
import pandas_datareader as pdr
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import datetime as datetime
import Imgur
from matplotlib.font_manager import FontProperties # 設定字體
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

def get_stock_name(stockNumber):
    try:
        url = 'https://tw.stock.yahoo.com/q/q?s=' + stockNumber
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find_all(text='成交')[0].parent.parent.parent
        stock_name = table.select('tr')[1].select('td')[0].text.strip('加到投資組合')
        return stock_name
    except:
        return "no"

def show_pic(msg):
    stockNumberList = msg.strip('比較').replace("/", ",").split(",")
    stockList = msg.strip('比較').replace("/", ".TW/").split("/") # 股票代號(有.TW)
    stockList[-1] += ".TW" 
    nameList = [] # 股票名稱
    for k in range(len(stockList)):
        nameList.append(get_stock_name(stockNumberList[k]))
    end = datetime.datetime.now()
    date = end.strftime("%Y%m%d")
    year = str(int(date[0:4]) - 1)
    month = date[4:6]
    df_stock = pdr.DataReader(stockList, 'yahoo', start= year+"-"+month,end=end)
    adjClose = df_stock['Close']
    for i in range(len(stockList)):
        adjClose[stockList[i]].plot(label=nameList[i])
    plt.ylabel('股價', fontsize=30, fontproperties=font_path)
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.legend(fontsize=14,  prop=font_path)
    plt.grid(True, axis='y') # 網格線
    plt.savefig("比較" + '.png') #存檔
    plt.show()
    plt.close() # 殺掉記憶體中的圖片
    return Imgur.showImgur("比較")
