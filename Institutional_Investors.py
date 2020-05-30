''' 
三大法人買賣超
'''
#繪圖用
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
import datetime
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
from matplotlib.font_manager import FontProperties # 設定字體
import Imgur
import time
# from matplotlib.ticker import FuncFormatter
chinese_font = matplotlib.font_manager.FontProperties(fname='msjh.ttf') # 引入同個資料夾下支援中文字檔
chinese_title = matplotlib.font_manager.FontProperties(fname='msjh.ttf', size=24) 
chinese_subtitle = matplotlib.font_manager.FontProperties(fname='msjh.ttf', size=20) 

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


# 畫出籌碼面圖
def institutional_investors_pic(stockNumber):
    stock_name = get_stock_name(stockNumber)
    if stock_name == "no": return "股票代碼錯誤!"
    mn=pd.read_html(f'https://www.cnyes.com/twstock/Institutional/{stockNumber}.htm')
    st=pd.read_html(f'https://www.cnyes.com/twstock/ps_historyprice/{stockNumber}.htm')
    mn=mn[0]
    #fig=plt.figure(24,20)
    rg=len(mn['合計'])-1
    st= st[0]["收盤"][0:rg+1]
    st_hist=list(st)
    st_hist.reverse()
    mm_hist= list(mn['合計'])
    mm_hist.reverse()
    mm_dt=list(mn['日期'])
    mm_dt.reverse()
    fig,ax1 = plt.subplots(figsize=(16, 7))
    plt.title(stock_name + " 三大法人買賣超", FontProperties=chinese_title)
    ax1.bar(mm_dt,mm_hist,0.4,alpha=0.8)
    ax1.set_ylabel("張", FontProperties=chinese_subtitle, rotation=360)
    plt.grid(True,linestyle="--",color='gray',linewidth='0.5',axis='both')
    ax2=ax1.twinx()
    ax2.plot(st_hist,color='r',linewidth='2.5')
    ax2.set_ylabel('股價(元)', FontProperties=chinese_subtitle)
    plt.grid(True,linestyle="--",color='gray',linewidth='0.5',axis='both')
    plt.legend(prop=chinese_subtitle)
    plt.savefig("法人.png")
    plt.show()
    plt.close()
    return Imgur.showImgur("法人")
# 三大法人買賣超(純文字敘述)
def institutional_investors(stockNumber):
    time.sleep(2)
    # today=datetime.date.today()
    # date=today.strftime('20%y%m%d') #date = '20191108'
    r = requests.get('https://www.twse.com.tw/fund/T86?response=csv&date&selectType=ALLBUT0999')
    df = pd.read_csv(StringIO(r.text), header=1).dropna(how='all', axis=1).dropna(how='any')
    columns = len(df["證券代號"])-1
    for i in range(columns):
        stockCode = df["證券代號"][i]
        if stockCode == stockNumber:
            content = df["證券名稱"][i] + "\n" + "外陸資買進張數(不含外資自營商): " + str(round(int(df["外陸資買進股數(不含外資自營商)"][i].replace(',',''))/1000))+"張\n"
            content += "外陸資賣出張數(不含外資自營商): " + str(round(int(df["外陸資賣出股數(不含外資自營商)"][i].replace(',',''))/1000))+"張\n"
            content += "外陸資買賣超張數(不含外資自營商): " + str(round(int(df["外陸資買賣超股數(不含外資自營商)"][i].replace(',',''))/1000))+"張\n--------------------------\n"
            content += "投信買進張數: " + str(round(int(df["投信買進股數"][i].replace(',',''))/1000))+"張\n"
            content += "投信賣出張數: " + str(round(int(df["投信賣出股數"][i].replace(',',''))/1000))+"張\n"
            content += "投信買賣超張數: " + str(round(int(df["投信買賣超股數"][i].replace(',',''))/1000))+"張\n--------------------------\n"
            content += "自營商買進張數(自行買賣): " + str(round(int(df["自營商買進股數(自行買賣)"][i].replace(',',''))/1000))+"張\n"
            content += "自營商賣出張數(自行買賣): " + str(round(int(df["自營商賣出股數(自行買賣)"][i].replace(',',''))/1000))+"張\n"
            content += "自營商買賣超張數(自行買賣): " + str(round(int(df["自營商買賣超股數(自行買賣)"][i].replace(',',''))/1000))+"張\n--------------------------\n"
            content += "自營商買進張數(避險): " + str(round(int(df["自營商買進股數(避險)"][i].replace(',',''))/1000))+"張\n"
            content += "自營商賣出張數(避險): " + str(round(int(df["自營商賣出股數(避險)"][i].replace(',',''))/1000))+"張\n"
            content += "自營商買賣超張數(避險): " + str(round(int(df["自營商買賣超股數(避險)"][i].replace(',',''))/1000))+"張\n\n"
            content += "三大法人買賣超張數:" + str(round(int(df["三大法人買賣超股數"][i].replace(',',''))/1000))+"張\n"
            return content
