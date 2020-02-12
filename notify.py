import schedule
import time
import datetime
from bs4 import BeautifulSoup
import requests
import twder
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import urllib.parse
from pymongo import MongoClient

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Your Channel Access Token')
yourID='Your User ID'

# Authentication Database認證資料庫
stockDB='mystock'
currencyDB = 'mycurrency'
currency_list = { 
    "USD" : "美元",
    "JPY": "日圓",
    "HKD" :"港幣",
     "GBP": "英鎊",
     "AUD": "澳幣",
     "CAD" : "加拿大幣",
    "CHF" : "瑞士法郎",  
    "SGD" : "新加坡幣",
    "ZAR" : "南非幣",
    "SEK" : "瑞典幣",
    "NZD" : "紐元", 
    "THB" : "泰幣", 
    "PHP" : "菲國比索", 
    "IDR" : "印尼幣", 
    "KRW" : "韓元",   
    "MYR" : "馬來幣", 
    "VND" : "越南盾", 
    "CNY" : "人民幣",   
}

##### 資料庫連接 #####
def constructor_stock():
    client = MongoClient("URL")
    db = client[stockDB]
    return db
def constructor_currency():
    client = MongoClient("URL")
    db = client[currencyDB]
    return db

# 查詢匯率
def showCurrency(msg):
    content = ""
    # 資料格式 {貨幣代碼: (時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...}
    currency = twder.now(msg) 
    currency_name = currency_list[msg] # 取得對應的貨幣名稱
    # 當下時間
    now_time = str(currency[0])
    # 銀行現金買入價格
    buying_cash = "無資料" if  currency[1] == '-' else str(float(currency[1]))
    # 銀行現金賣出價格
    sold_cash = "無資料" if  currency[2] == '-' else str(float(currency[2])) 
    # 銀行即期買入價格
    buying_spot = "無資料" if  currency[3] == '-' else str(float(currency[3]))
    # 銀行即期賣出價格
    sold_spot = "無資料" if  currency[4] == '-' else str(float(currency[4])) 

    content += currency_name + "最新掛牌時間為: " + now_time + '\n ---------- \n 現金買入價格: ' + buying_cash + '\n 現金賣出價格: ' + str(sold_cash) + '\n 即期買入價格: ' + buying_spot + '\n 即期賣出價格: '  +  sold_spot + '\n \n'
    return content
  
# 抓使用者設定它關心的股票
def cache_users_stock():
    db=constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'stock'}))
        users.append(cel)
    return users
# cache_users_stock()

# 抓使用者設定它關心的股票
def cache_users_currency():
    db=constructor_currency()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'currency'}))
        users.append(cel)
    return users

def look_currency_price(currency, condition, price, userID):
    print(userID)
    realtime_currency = (twder.now(currency))[4]
    currency_name = currency_list[currency]
    content = currency_name + "當前即期賣出價格為: " + str(realtime_currency)
    if condition == '<':
         content += "\n篩選條件為: < "+ price
         if float(realtime_currency) < float(price):
            content += "\n符合" + realtime_currency + " < " + price + "的篩選條件"
            line_bot_api.push_message(userID, TextSendMessage(text=content))
    elif condition == '>':
         content += "\n篩選條件為: > "+ price
         if float(realtime_currency) > float(price):
            content += "\n符合" + realtime_currency + " > " + price + "的篩選條件"
            line_bot_api.push_message(userID, TextSendMessage(text=content))
    elif condition == "=":
        content += "\n篩選條件為: = "+ price
    # elif condition == "未設定":
    #     content += "\n尚未設置篩選條件, 請設定您想要的目標價格條件,如: 新增外幣"+currency+">10"
    
    # else:
    #     content += "\n無法判定此外幣設定的篩選條件"
    # line_bot_api.push_message(userID, TextSendMessage(text=content))

# print(cache_users_currency())
def job_currency():
    dataList = cache_users_currency()
    for i in range(len(dataList)):
        for k in range(len(dataList[i])):
            look_currency_price(dataList[i][k]['favorite_currency'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
job_currency()

# 查看當前股價
def look_stock_price(stock, condition, price, userID):
    print(userID)
    url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getstock= soup.findAll('b')[1].text
    content = stock + "當前股市價格為: " +  getstock
    if condition == '<':
         content += "\n篩選條件為: < "+ price
         if float(getstock) < float(price):
            content += "\n符合" + getstock + " < " + price + "的篩選條件"
            line_bot_api.push_message(userID, TextSendMessage(text=content))
    elif condition == '>':
         content += "\n篩選條件為: > "+ price
         if float(getstock) > float(price):
            content += "\n符合" + getstock + " > " + price + "的篩選條件"
            line_bot_api.push_message(userID, TextSendMessage(text=content))
    elif condition == "=":
        content += "\n篩選條件為: = "+ price
        if float(getstock) < float(price):
             content += "\n符合" + getstock + " = " + price + "的篩選條件"
             line_bot_api.push_message(userID, TextSendMessage(text=content))
    # elif condition == "":
    #     content += "\n尚未設置篩選條件, 請設定您想要的目標價格條件,如: 關注"+stock+">100"
    # else:
    #     content += "\n無法判定此檔股票設定的篩選條件"
    # line_bot_api.push_message(userID, TextSendMessage(text=content))

# look_stock_price(stock='2002', condition='>', price=31)
def job():
    dataList = cache_users_stock()
    # print(dataList)
    for i in range(len(dataList)):
        for k in range(len(dataList[i])):
            # print(dataList[i][k])
            look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])

# second_5_j = schedule.every(5).seconds.do(job)
# second_5_j = schedule.every().day.at("22:04").do(job)  # 特定時間推播
