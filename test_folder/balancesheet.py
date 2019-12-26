import yfinance as yf
import time
import pandas as pd
import requests as re
from bs4 import BeautifulSoup
stock = yf.Ticker('2330.TW')
stock_info = yf.Ticker('2330.TW').info
balance_sheet = stock.balance_sheet
# print(stock_info)

# 將 yfinance 有提供的數據項目取出存在 info_columns，它將會成為 stk_info_df 這張總表的欄位項目
info_columns = list(stock_info.keys())
# print(info_columns)
# 創立一個名為 stk_info_df 的總表，用來存放所有股票的基本資料！其中 stk_list 是我們先前抓到的股票代碼喔！
# stock_df = pd.DataFrame(stock.balance_sheet, columns = info_columns)
# print(stock_df)

print(balance_sheet)
# soup = BeautifulSoup(re.get("http://slickcharts.com/sp500").text, "html5lib")
# content = soup.find_all('table')[0].find_all('tr')[1:]

# name_list = []
# label_list = []
# weight_list = []

# for i in content:
#     name_list.append(i.find_all('td')[1].get_text())
#     label_list.append(i.find_all('td')[2].get_text().replace('.','-'))
#     weight_list.append(float(i.find_all('td')[3].get_text()))
    
# df = pd.DataFrame({'name': name_list, 'label': label_list, 'weight': weight_list})
# print(df)

