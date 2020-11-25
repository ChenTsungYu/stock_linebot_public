import twder
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import Imgur
import numpy as np
import matplotlib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from matplotlib.font_manager import FontProperties # 設定字體
chinese_font = matplotlib.font_manager.FontProperties(fname='msjh.ttf') # 引入同個資料夾下支援中文字檔

def getCurrencyName(currency):
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
    try: currency_name = currency_list[currency]
    except: return "無可支援的外幣"
    return currency_name
# 外幣兌換
def exchange_currency(code) :
    condition = code[0:2] # 買入或賣出
    code = code.strip(code[0:4])
    currency = code[0:3] # 外幣代號
    currency_name = getCurrencyName(currency)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    amount = float(code[3:])
    currency = twder.now(currency) 
    now_time = str(currency[0]) # 當下時間
    content = currency_name + "最新掛牌時間為: " + now_time
    if condition == "賣出": # 銀行即期買入價格  # 使用者想賣外幣
        buying_spot = "無資料" if  currency[3] == '-' else float(currency[3]) # if-else簡寫
        if buying_spot == "無資料": return "此外幣無即期買入匯率"
        outcome = str( '%.2f ' % (amount * buying_spot))
        content +=  '\n即期買入價格: ' + str(buying_spot)
    else:   # 銀行即期賣出價格 # 使用者想買外幣
        sold_spot = "無資料" if  currency[4] == '-' else float(currency[4]) # if-else簡寫
        if sold_spot == "無資料": return "此外幣無即期賣出匯率"
        outcome = str( '%.2f ' % (amount * sold_spot))
        content +=  f'\n即期賣出價格: {sold_spot}'

    content += f"\n換匯結果為台幣 {outcome}元"
    return content

# 查詢匯率
def showCurrency(code) -> "JPY": # code 為外幣代碼
    content = ""
    currency_name = getCurrencyName(code)
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    # 資料格式 {貨幣代碼: (時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...}
    currency = twder.now(code) 
    # 當下時間
    now_time = str(currency[0])
    # 銀行現金買入價格
    buying_cash = "無資料" if currency[1] == '-' else str(float(currency[1])) 
    # 銀行現金賣出價格
    sold_cash = "無資料" if currency[2] == '-' else str(float(currency[2])) 
    # 銀行即期買入價格
    buying_spot = "無資料" if currency[3] == '-' else str(float(currency[3])) 
    # 銀行即期賣出價格
    sold_spot = "無資料" if currency[4] == '-' else str(float(currency[4])) 

    content +=  f"{currency_name} 最新掛牌時間為: {now_time}\n ---------- \n 現金買入價格: {buying_cash}\n 現金賣出價格: {sold_cash}\n 即期買入價格: {buying_spot}\n 即期賣出價格: {sold_spot}\n \n'
    return content
    
##--------------------------------------------
#######     走勢圖
#   即期匯率
def spot_exrate_sixMonth(code2):
    currency_name = getCurrencyName(code2)# 取得對應的貨幣名稱
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    dfs = pd.read_html(f'https://rate.bot.com.tw/xrt/quote/l6m/{code2}')
    currency = dfs[0].iloc[:, 0:6] # 獲取前6個欄位
    # 更改欄位名稱
    currency.columns = [u'Date', u'Currency', u'現金買入', u'現金賣出', u'即期買入',  u'即期賣出']
    currency[u'Currency'] = currency[u'Currency'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1] #  row 順序反轉，因原始資料是從最新開始排
    if currency["即期買入"][0] == "-" or currency["即期買入"][0] == 0.0:
        return "即期匯率無資料可分析"
    currency.plot(kind = 'line', figsize=(12, 6),x='Date', y=[u'即期買入', u'即期賣出'])
    plt.legend(prop=chinese_font) # 支援中文字
    plt.title(f"{currency_name} 即期匯率",  fontsize=20, fontproperties=chinese_font)
    plt.savefig(f"{code2}.png")
    plt.show()
    plt.close()
    return Imgur.showImgur(code2)

#  現金匯率
def cash_exrate_sixMonth(code1) -> "USA":
    currency_name = getCurrencyName(code1)# 取得對應的貨幣名稱
    if currency_name == "無可支援的外幣": return "無可支援的外幣"
    dfs = pd.read_html(f'https://rate.bot.com.tw/xrt/quote/l6m/{code1}')
    currency = dfs[0].iloc[:, 0:6]
    # 更改欄位名稱
    currency.columns = [u'Date', u'Currency', u'現金買入', u'現金賣出', u'即期買入',  u'即期賣出']
    currency[u'Currency'] = currency[u'Currency'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1] #  row 順序反轉，因原始資料是從最新開始排
    if currency["現金買入"][0] == "-" or currency["現金買入"][0]== 0.0:
        return "現金匯率無資料可分析"
    currency.plot(kind = 'line', figsize=(12, 6), x='Date', y=[u'現金買入', u'現金賣出'])
    plt.legend(prop=chinese_font) # 支援中文字
    plt.title(currency_name + " 現金匯率",  fontsize=20, fontproperties=chinese_font)
    plt.savefig(f"{code1}.png")
    plt.show()
    plt.close()
    return Imgur.showImgur(code1)

# print(cash_exrate_sixMonth(code1))


def get_currency_list():
    currency_list = twder.now_all()
    currency_list = list(currency_list.values())
    currencies = []
    for i in range(len(currency_list)):
        currencies.append(currency_list[i][4])
    return currencies

'''
補充：
Coninbase提供的endpoint，不需API Key，不過只有查詢即時匯率的功能，
若要其他功能，需要API Key，教學參考HackMD文件鏈結，有官方教學
'''
def getExchangeRate(msg): # 不同貨幣直接換算(非只限於台幣)
    """
    sample
    code = '換匯USD/TWD/100;
    code = '換匯USD/JPY/100'
    """
    currency_list = msg[2:].split("/")
    currency = currency_list[0] # 輸入想查詢的匯率
    currency1 = currency_list[1] # 輸入想兌換的匯率
    money_value = currency_list[2] # 輸入金額數值
    url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency
    res = requests.get(url_coinbase)
    jData = res.json()
    pd_currency = jData['data']['rates']
    content = f'目前的兌換率為:{pd_currency[currency1]} {currency1} \n查詢的金額為: '
    amount =  float(pd_currency[currency1]) 
    content += str('%.2f' % (amount * float(money_value))) + " " +currency1
    return content
