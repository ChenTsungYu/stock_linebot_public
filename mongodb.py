''' 
個人股票、外匯清單
'''
from pymongo import MongoClient
import urllib.parse
import datetime
import stockprice
import EXRate
from EXRate import *
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
    
# Authentication Database認證資料庫
stockDB='mystock'
currencyDB = 'mycurrency'
# DB  connection
def constructor_stock(): 
    client = MongoClient("URL")
    db = client[stockDB]
    return db

def constructor_currency():
    client = MongoClient("URL")
    db = client[currencyDB]
    return db

# ---------------------------- 新增 修改 刪除前 先確認股票清單中是否有該檔股票--------------------------
def query_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    dataList = collect.find_one({"favorite_stock": stockNumber})
    if dataList == None:
        print("none")
    return dataList

#----------------------------更新暫存的股票名稱--------------------------
def update_my_stock(user_name,  stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition':condition , "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content

# ----------------  秀出使用者的股票清單       ----------------
def show_my_stock(userID, user_name, msg):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的股票清單為空，請透過指令新增股票至清單中"
    content = ""
    for i in range(len(dataList)):
        content += stockprice.getprice(dataList[i]["favorite_stock"], msg)
    return content
#   -----------    新增使用者的股票       -------------
def write_my_stock(userID, user_name, stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition , target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition" :  condition,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
        return f"{stockNumber}已新增至您的股票清單"
        
# ----------------  刪除使用者特定的股票       ----------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"

# ----------------  刪除使用者股票清單內所有的股票       ----------------
def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return "全部股票刪除成功"

# ----------------  秀出使用者的股票條件       ----------------
def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的股票清單為空，請透過指令新增股票至清單中"
    content = "您清單中的選股條件為: \n"
    for i in range(len(dataList)):
        content += f'{dataList[i]["favorite_stock"]} {dataList[i]["condition"]} {dataList[i]["price"]}\n'
    return content

#----------------------------  更新匯率清單的匯率  --------------------------
def update_my_currency(user_name, currency, condition , target_price):
    db=constructor_currency()
    collect = db[user_name]
    collect.update_many({"favorite_currency": currency }, {'$set': {'condition':condition , "price": target_price}})
    return f"{currency_list[currency]}更新成功"

#----------------------------  新增匯率至匯率清單  --------------------------
def write_my_currency(userID , user_name, currency, condition, target_price):
    db = constructor_currency()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_currency": currency})
    content = ""
    if is_exit != None : return update_my_currency(user_name, currency, condition , target_price)
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_currency": currency,
                "condition" :  condition,
                "price" : target_price,
                "tag": "currency",
                "date_info": datetime.datetime.now()
            })
        return f"{currency_list[currency]}已新增至您的外幣清單"

#----------------------------  查詢匯率清單的匯率(文字)  --------------------------
def show_my_currency(userID, user_name):
    db = constructor_currency()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content = ""
    for i in range(len(dataList)):
        content += EXRate.showCurrency(dataList[i]["favorite_currency"]) 
    return content


# ----------------  刪除使用者清單特定的匯率       ----------------
def delete_my_currency(user_name, currency):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_one({'favorite_currency': currency})
    return currency_list[currency] + "刪除成功"


#----------------------------  刪除匯率清單全部匯率  --------------------------
def delete_my_allcurrency(user_name, userID):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return "外幣清單已清空"

# ----------------  查詢使用者的匯率設定條件       ----------------
def show_currency_setting(user_name, userID):
    db = constructor_currency()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content = "您清單中外幣篩選條件為: \n"
    for i in range(len(dataList)):
        content += f'{dataList[i]["favorite_currency"]} {dataList[i]["condition"]} {dataList[i]["price"]}\n'
    return content
