import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import yfinance as yf # yahoo專用的拿來拉股票資訊
import datetime
import talib #技術分析專用
# from talib import *
# from talib import abstract
import mpl_finance as mpf # 專門用來畫蠟燭圖的
import matplotlib.pyplot as plt # 繪圖專用
import Imgur
###############################################################################
#                              股票機器人 技術面分析                            #
###############################################################################
#設定顏色
color=['#2196f3','#4caf50','#ffc107','#f436c7','#f27521','#e00b0b']

def TheConstructor(userstock):
    # 設定要的資料時間
    start = datetime.datetime.now() - datetime.timedelta(days=365) #先設定要爬的時間
    end = datetime.date.today()
    
    # 與yahoo請求
    pd.core.common.is_list_like = pd.api.types.is_list_like
    yf.pdr_override()
    
    # 取得股票資料
    try:
        stock = data.get_data_yahoo(userstock+'.TW', start, end)

    except :
        # 如果失敗回傳"失敗"這張圖
        stock = 'https://i.imgur.com/RFmkvQX.jpg'
        
    return stock



#---------------------------------------- 股票K線圖 ------------------------------------

def stock_Candlestick(userstock):
    stock=TheConstructor(userstock)
    
    if type(stock) == str:
        return stock
    else:
        fig = plt.figure(figsize=(24, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xticks(range(0, len(stock.index), 5))
        ax.set_xticklabels(stock.index[::5])
        plt.xticks(fontsize=10,rotation=90)
        mpf.candlestick2_ochl(ax, stock['Open'], stock['Close'], stock['High'], stock['Low'],
                             width=0.5, colorup='r', colordown='green',
                             alpha=0.6)
        plt.title("Candlestick_chart") # 標題設定
        plt.grid(True,axis='y')
        plt.savefig('Candlestick_chart.png') #存檔
        plt.close() # 刪除記憶體中的圖片
        
        return Imgur.showImgur('Candlestick_chart')

# userstock = "2330"
# stock_Candlestick(userstock)
#---------------------------------------- KD指標 ------------------------------------
def stock_KD(userstock):
    stock=TheConstructor(userstock)
    
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(list(talib.STOCH(stock['High'], stock['Low'], stock['Close']))).transpose()
        ret = pd.concat([ret,stock['Close']], axis=1)
        ret.columns=['K','D','Close']
        ret.index = stock['Close'].index
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('KD') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('KD.png') #存檔
        plt.close() # 刪除記憶體中的圖片
        return Imgur.showImgur('KD') 
    
# userstock = "2330"
# stock_KD(userstock)    
#-------------------------------- 移動平均線（Moving Average）------------------------------------
def stock_MA(userstock):
    stock=TheConstructor(userstock)
    
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.SMA(stock['Close'],10), columns= ['10-day average']) #10日移動平均線
        ret = pd.concat([ret,pd.DataFrame(talib.SMA(stock['Close'],20), columns= ['20-day average'])], axis=1) #10日移動平均線
        ret = pd.concat([ret,pd.DataFrame(talib.SMA(stock['Close'],60), columns= ['60-day average'])], axis=1) #10日移動平均線
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Moving_Average') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Moving_Average.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Moving_Average') 

# userstock = "2330"
# stock_MA(userstock)         
#-------------------- 指數平滑異同移動平均線（Moving Average Convergence / Divergence）------------------------------------
def stock_MACD(userstock):
    stock=TheConstructor(userstock)
    ret=pd.DataFrame()
    
    if type(stock) == str:
        return stock
    else:

        ret['MACD'],ret['MACDsignal'],ret['MACDhist'] = talib.MACD(stock['Close'],fastperiod=6, slowperiod=12, signalperiod=9)
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('MACD') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('MACD.png') #存檔
        plt.close() # 刪除記憶體中的圖片
        return Imgur.showImgur('MACD') 

# userstock = "2330"
# stock_MACD(userstock) 
#------------------------ 能量潮指標（On Balance Volume）------------------------------------
def stock_OBV(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.OBV(stock['Close'], stock['Volume']), columns= ['OBV'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('On_Balance_Volume') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('On_Balance_Volume.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('On_Balance_Volume') 
        

#------------------------ 威廉指數（Williams Overbought）------------------------------------
def stock_William(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.WILLR(stock['High'], stock['Low'], stock['Open']), columns= ['Williams'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Williams_Overbought') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Williams_Overbought.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Williams_Overbought') 
        

#------------------------ 平均真實區域指標（Average True Range）------------------------------------
def stock_ATR(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.ATR(stock['High'], stock['Low'], stock['Close']), columns= ['Average True Range'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Average_True_Range') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Average_True_Range.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Average_True_Range') 
        

#------------------------ 平均趨向指標（Average Directional Indicator）------------------------------------
def stock_ADX(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.ADX(stock['High'], stock['Low'], stock['Close']), columns= ['Average True Range'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Average_Directional_Indicator') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Average_Directional_Indicator.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Average_Directional_Indicator') 
        

#------------------------ 相對強弱指數（Relative Strength Index）------------------------------------
def stock_RSI(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        # RSI的天數設定一般是6, 12, 24
        ret = pd.DataFrame(talib.RSI(stock['Close'],6), columns= ['Relative Strength Index'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title(userstock + 'RSI') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Relative_Strength_Index.png') #存檔
        plt.close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Relative_Strength_Index') 
# stock_RSI("2330")

#------------------------ 資金流動指標（Money Flow Index）------------------------------------
def stock_MFI(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.MFI(stock['High'],stock['Low'],stock['Close'],stock['Volume'], timeperiod=14), columns= ['Money Flow Index'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Money_Flow_Index') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Money_Flow_Index.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Money_Flow_Index') 

#------------ 接收者操作特徵曲線（Receiver Operating Characteristic Curve）------------------------------------
def stock_ROC(userstock):
    stock=TheConstructor(userstock)
    if type(stock) == str:
        return stock
    else:
        ret = pd.DataFrame(talib.ROC(stock['Close'], timeperiod=10), columns= ['Receiver Operating Characteristic curve'])
        ret = pd.concat([ret,stock['Close']], axis=1)
        
        ### 開始畫圖 ###
        ret.plot(color=color, linestyle='dashed')
        ret['Close'].plot(secondary_y=True,color=color[5])
        plt.title('Receiver_Operating_Characteristic_Curve') # 標題設定
        plt.grid(True,axis='y')
        plt.show()
        plt.savefig('Receiver_Operating_Characteristic_Curve.png') #存檔
        plt. close() # 刪除記憶體中的圖片
        return Imgur.showImgur('Receiver_Operating_Characteristic_Curve') 

  