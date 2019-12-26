'''
此檔仍在測試
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import json
import Imgur
import datetime

###############################################################################
#                              股票機器人 標準差分析                            #
###############################################################################
today = datetime.date.today()

def stockSD(stocknumber):
    url = 'https://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '&Odate=' + str(datetime.date.today()) + '&Period=3.5&is_log=0&is_adjclose=0'
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    # if len(getjson)>10: # 如果資料不到10筆，表示請求失敗
    #     # 不知為何，有些股票的網址不一樣，因此上面的網址請求失敗，要在試試下面這個
    #     url = 'https://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '&Odate=' + str(datetime.date.today()) + '&Period=3.5&is_log=0&is_adjclose=0'
    #     list_req = requests.get(url)
    #     soup = BeautifulSoup(list_req.content, "html.parser")
    # getjson=json.loads(soup.text)
    if len(getjson)>10: # 如果資料不到10筆，表示請求失敗
        time=[]  
        theClose=[]
        TL=[]
        TL1=[]
        TL2=[]
        TL3=[]
        TL4=[]
        # 先把所有要畫圖的資料準備好
        for i in range(1,len(getjson),10):
            time.append(getjson[str(i)]['theDate_O'])
            theClose.append(getjson[str(i)]['theClose'])
            TL.append(getjson[str(i)]['TL'])
            TL1.append(getjson[str(i)]['TL']+getjson[str(i)]['STD']*2)
            TL2.append(getjson[str(i)]['TL']+getjson[str(i)]['STD'])
            TL3.append(getjson[str(i)]['TL']-getjson[str(i)]['STD'])
            TL4.append(getjson[str(i)]['TL']-getjson[str(i)]['STD']*2)
           
        ##################### 繪 圖 #####################
        #把文字設定為中文
        plt.plot(time,TL) # 中央平均線
        plt.plot(time,TL1) # 加兩個標準差
        plt.plot(time,TL2) # 加一個標準差
        plt.plot(time,TL3) # 減一個標準差
        plt.plot(time,TL4) # 減兩個標準差
        plt.plot(time,theClose) # 每日的收盤假
        plt.scatter(getjson[str(len(getjson))]['theDate_O'],getjson[str(len(getjson))]['theClose'], marker = 'o', color = 'r', label='5', s = 15) # 最後一天的股價，因為上面for迴圈是用跳的，可能會跳過最後一個點
        plt.text(getjson[str(len(getjson))]['theDate_O'], getjson[str(len(getjson))]['theClose'], '%s' % getjson[str(len(getjson))]['theDate_O']+' price', fontsize=10 ) # 最後一天的點上方的標籤文字
        plt.xticks(fontsize=5,rotation=90) # 設定x軸標籤
        plt.title('Standard Deviation', fontsize=20)
        plt.xlabel("Time (3.5 year)", fontsize=15)
        plt.ylabel("Price", fontsize=15)
        plt.show()
        plt.savefig('showSD.png')
        plt.close() # 殺掉記憶體中的圖片
        #開始利用imgur幫我們存圖片，以便於等等發送到手機
        return Imgur.showImgur('showSD')
    else:
        # 找不到這個股票也回傳"失敗"這張圖
        return 'https://i.imgur.com/RFmkvQX.jpg' 
    

# 股票搜尋
def searchstock(stocknumber):
    url = 'https://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '.TW&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    if len(getjson)>10:
        url = 'https://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'
        list_req = requests.get(url)
        soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    if len(getjson)>10:
        time = getjson[str(len(getjson))]['theDate_O']
        print('時間 = ' + time)

        theClose = getjson[str(len(getjson))]['theClose']
        print('收盤價 = ' + str(theClose))

        TL = getjson[str(len(getjson))]['TL']
        print('TL = ' + str(TL))

        STD = getjson[str(len(getjson))]['STD']
        print('STD = ' + str(STD))
    
        low="很貴不要買"
        if (TL - STD*2) >= theClose:
            low ="非常便宜趕快買"
        elif (TL - STD) >= theClose:
            low ="蠻便宜了"
    
        return('收盤價 = ' + str(theClose) + '\n中間價 = ' + str(TL) + '\n線距 = ' + str(STD) + '\n' + low)
    else:
        return('沒有這個股票')

# stocknumber = '2330'
# stockSD(stocknumber)