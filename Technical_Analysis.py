import pandas as pd
import matplotlib
matplotlib.use('Agg')
import talib
from talib import abstract
import Imgur
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import requests,datetime
from bs4 import BeautifulSoup
from matplotlib.font_manager import FontProperties # 設定字體
chinese_font = matplotlib.font_manager.FontProperties(fname='msjh.ttf') # 引入同個資料夾下支援中文字檔

def general_df(stockNumber):
    stockNumberTW  =  stockNumber + ".TW"
    df_x=pdr.DataReader(stockNumberTW,'yahoo',start="2019")
    df_x.rename(columns = {'Open':'open', 'High':'high', 'Low':'low', 'Close':'close'}, inplace = True)
    return df_x

def get_stockName(stockNumber):
    url = 'https://tw.stock.yahoo.com/q/q?s='+stockNumber
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all(text='成交')[0].parent.parent.parent
    stock_name = table.select('tr')[1].select('td')[0].text
    stock_name = stock_name.strip('加到投資組合')
    return stock_name

def MACD_pic(stockNumber, msg):
    stock_name = get_stockName(stockNumber)
    df_x = general_df(stockNumber)
    jj=df_x.reset_index(drop=False)
    abstract.MACD(df_x).plot(figsize=(16,8))
    plt.xlabel("date",  FontProperties=chinese_font)
    plt.ylabel("Value",  FontProperties=chinese_font)
    plt.grid(True,axis='y')
    plt.title(stock_name+"MACD線" ,FontProperties=chinese_font)
    plt.savefig(msg + ".png")
    plt.close()
    return Imgur.showImgur(msg)

# ===================================
# KD指標
def RSI_pic(stockNumber, msg):
    stock_name = get_stockName(stockNumber)
    df_x = general_df(stockNumber)
    jj=df_x.reset_index(drop=False)
    abstract.RSI(df_x).plot(figsize=(16,8))
    plt.xlabel("date",  FontProperties=chinese_font)
    plt.ylabel("KD值",  FontProperties=chinese_font)
    plt.grid(True,axis='y')
    plt.title(stock_name+"KD線" ,FontProperties=chinese_font)
    plt.savefig(msg + ".png")
    plt.close()
    return Imgur.showImgur(msg)

# ===================================
# BBand分析
def BBANDS_pic(stockNumber, msg):
    stock_name = get_stockName(stockNumber)
    df_x = general_df(stockNumber)
    jj=df_x.reset_index(drop=False)
    abstract.BBANDS(df_x).plot(figsize=(16,8))
    plt.xlabel("date",  FontProperties=chinese_font)
    plt.ylabel("價格",  FontProperties=chinese_font)
    plt.grid(True,axis='y')
    plt.title(stock_name+"BBANDS" ,FontProperties=chinese_font)
    plt.savefig(msg + ".png")
    plt.close()
    return Imgur.showImgur(msg)

