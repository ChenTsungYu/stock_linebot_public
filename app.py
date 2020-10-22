'''
Created by Tsung Yu on 17/03/2020.
Copyright © 2020 Tsung Yu. All rights reserved.
'''
import re
from pymongo import MongoClient
import pymongo
import urllib.parse
import EXRate
import news
import stockprice
import Institutional_Investors
import stock_compare
from msg_template import Msg_fundamental_ability
from msg_template import Msg_Template
from msg_template import questionnaire
from msg_template import Msg_Exrate
from msg_template import Msg_News
from msg_template import Msg_diagnose
import new_famous_book
import kchart
# import filter_stock
import Technical_Analysis
import Technical_Analysis_test
import Fundamental_Analysis
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('channl access token')
handler = WebhookHandler('secrect key ')
my_user_id = 'Your UserID'
line_bot_api.push_message(my_user_id, TextSendMessage(text="start"))
@app.route("/")
def home():
    return "home"
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID
#================================ 
    # 問卷
    if re.match("問卷分析", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.greeting_msg))
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q1))
        content = questionnaire.Q1_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("Q2", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q2))
        line_bot_api.push_message(uid, questionnaire.Q2_menu())
        return 0
    elif re.match("Q3", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q3))
        line_bot_api.push_message(uid, questionnaire.Q3_menu())
        return 0
    elif re.match("Q4", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q4))
        line_bot_api.push_message(uid, questionnaire.Q4_menu())
        return 0
    elif re.match("Q5", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q5))
        line_bot_api.push_message(uid, questionnaire.Q5_menu())
        return 0
    elif re.match("Q6", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q6))
        line_bot_api.push_message(uid, questionnaire.Q6_menu())
        return 0
    elif re.match("Q7", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q7))
        line_bot_api.push_message(uid, questionnaire.Q7_menu())
        return 0
    elif re.match("Q8", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q8))
        line_bot_api.push_message(uid, questionnaire.Q8_menu())
        return 0
    elif re.match("類型A", msg):
        img_url = questionnaire.type_A
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = questionnaire.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = questionnaire.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型C", msg):
        img_url = questionnaire.type_C
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型D", msg):
        img_url = questionnaire.type_D
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型E", msg):
        img_url = questionnaire.type_E
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型F", msg):
        img_url = questionnaire.type_F
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型G", msg):
        img_url = questionnaire.type_G
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型H", msg):
        img_url = questionnaire.type_H
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型I", msg):
        img_url = questionnaire.type_I
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型J", msg):
        img_url = questionnaire.type_J
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
#==========================================
    elif re.match("新書榜", msg):
        line_bot_api.push_message(uid, TextSendMessage("將給您最新理財新書......"))
        flex_message = Msg_Template.new_books()
        line_bot_api.push_message(uid, flex_message)
        return 0
    elif re.match("暢銷榜", msg):
        line_bot_api.push_message(uid, TextSendMessage("將給您最新理財暢銷書......"))
        flex_message = Msg_Template.famous_books()
        line_bot_api.push_message(uid, flex_message)
        return 0
#==========================================    
    elif re.match("/股票", msg):
        content = Msg_Template.menu_stock_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        content = Msg_Template.menu_etf_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("/理財", msg):
        content = Msg_Template.menu_fin_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("外匯列表", msg):
        content = Msg_Exrate.realtime_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("/外匯", msg):
        content = Msg_Template.menu_exrate_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("/我的收藏", msg):
        content = Msg_Template.menu_mylist_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("#股票健診", msg):
        content = Msg_diagnose.diagnose_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("/產業文章", msg):
        content = Msg_Template.industrial_artical()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("理財YOUTUBER推薦", msg):
        content = Msg_Template.youtube_channel()
        line_bot_api.push_message(uid, content)
        return 0
#===========================================    
    elif re.match('關注[0-9]{4}' ,msg): # 使用者新增股票至股票清單
        stockNumber = msg[2:6]
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": content = "股票代碼錯誤"
        else:
            line_bot_api.push_message(uid, TextSendMessage("加入股票代號"+stockNumber))
            if re.match('關注[0-9]{4}[<>][0-9]' ,msg):     
                content = mongodb.write_my_stock(uid, user_name , stockNumber, msg[6:7], msg[7:])
            else:
                content = mongodb.write_my_stock(uid, user_name , stockNumber, "未設定", "未設定")
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("股票教學", msg):
        content = Msg_Template.stock_info_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("外匯教學", msg):
        content = Msg_Exrate.Exrate_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("快樂學理財", msg):
        content = Msg_Template.learning_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("三大投資分析表", msg):
        img_url = "https://i.imgur.com/StGNRGR.png"
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("基本面", msg):
        content = Msg_Template.three_investment(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("技術面", msg):
        content = Msg_Template.three_investment(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("籌碼面", msg):
        content = Msg_Template.three_investment(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("保守型投資者", msg):
        content = Msg_Template.investor_type(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("激進型投資者", msg):
        content = Msg_Template.investor_type(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("獨立型投資者", msg):
        content = Msg_Template.investor_type(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("EPS", msg):
        content = Msg_Template.proper_noun(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("買超/賣超", msg):
        content = Msg_Template.proper_noun(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("多頭市場/空頭市場", msg):
        content = Msg_Template.proper_noun(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("黃金交叉/死亡交叉", msg):
        content = Msg_Template.proper_noun(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("理財電影", msg):
        content =Msg_Template.movies()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("理財書籍", msg):
        content = Msg_Template.fin_books()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("比較", msg): # 範例 : msg = '比較2330/2002/2317'
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 我們將會給您這幾檔股票收盤價走勢圖...'))
        img_url = stock_compare.show_pic(msg)
        if img_url == "no": line_bot_api.push_message(uid, TextSendMessage('股票代碼錯誤'))
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    elif re.match('#[0-9]', msg): #查詢某檔股票
        stockNumber = msg[1:]
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤"))
        else:          
            line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 查詢編號: {tockNumber} 的股價中...'))
            content_text = stockprice.getprice(stockNumber, msg)
            content = Msg_Template.stock_reply(stockNumber, content_text)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("三大面向分析[0-9]", msg):
        stockNumber = msg.strip("三大面向分析")
        content  = Msg_Template.stock_ananlysis_menu(stockNumber)
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match('股票技術面[0-9]', msg):
        stockNumber = msg.strip("股票技術面")
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 分析編號: {stockNumber}的股價中...'))
        content = Msg_Template.stock_tec_analysis(stockNumber)
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match('股票基本面[0-9]{4}', msg):
        stockNumber = msg.strip("股票基本面")
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 分析編號: {stockNumber}基本面中...'))
        content = Msg_Template.stock_fundation_analysis(stockNumber)
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("經營能力[0-9]{4}", msg):
        stockNumber = msg.strip("經營能力")
        stockName = stockprice.get_stock_name(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage(f"正在為您分析股票代號: {stockNumber} 的經營能力......"))
        if stockName == "no":
            content = "股票代碼錯誤"
            line_bot_api.push_message(uid, TextSendMessage(content))
        else:
            content = Msg_fundamental_ability.operating_ability(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("償債能力[0-9]{4}", msg):
        stockNumber = msg.strip("償債能力")
        stockName = stockprice.get_stock_name(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage(f"正在為您分析股票代號: {stockNumber} 的償債能力......"))
        if stockName == "no":
            content = "股票代碼錯誤"
            line_bot_api.push_message(uid, TextSendMessage(content))
        else:
            content = Msg_fundamental_ability.debt_ability(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("獲利能力[0-9]{4}", msg):
        stockNumber = msg.strip("獲利能力")
        stockName = stockprice.get_stock_name(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage(f"正在為您分析股票代號: {stockNumber} 的獲利能力......"))
        if stockName == "no":
            content = "股票代碼錯誤"
            line_bot_api.push_message(uid, TextSendMessage(content))
        else:
            content = Msg_fundamental_ability.profit_ability(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("排除地雷股健診", msg):
        line_bot_api.push_message(uid, TextSendMessage(f"u'\U0001F538' 請輸入地雷股+股票代碼，如「地雷股2002」，即可快速了解該個股是否值得投資!"))
        return 0
    elif re.match("定存股健診", msg):
        line_bot_api.push_message(uid, TextSendMessage(f"u'\U0001F538' 請輸入定存股+股票代碼，如「定存股2002」，即可快速了解該個股是否值得投資!"))
        return 0
    elif re.match("成長股健診", msg):
        line_bot_api.push_message(uid, TextSendMessage(f"u'\U0001F538' 請輸入成長股+股票代碼，如「成長股2002」，即可快速了解該個股是否值得投資!"))
        return 0
    elif re.match("便宜股健診", msg):
        line_bot_api.push_message(uid, TextSendMessage(f"u'\U0001F538' 請輸入便宜股+股票代碼，如「便宜股2002」，即可快速了解該個股是否值得投資!"))
        return 0
    elif re.match("地雷股[0-9]{4}", msg):
        stockNumber = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 正在為您做股票編號: {stockNumber}地雷股排除健診...'))
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤"))
        else:
            content = Msg_diagnose.mine_stock_menu(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("成長股[0-9]{4}", msg):
        stockNumber = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 正在為您做股票編號: {stockNumber}成長股健診...'))
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤"))
        else:
            content = Msg_diagnose.growth_stock_menu(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("定存股[0-9]{4}", msg):
        stockNumber = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 正在為您做股票編號: {stockNumber} 定存股健診...'))
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤"))
        else:
            content = Msg_diagnose.fixed_deposit_stock_menu(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("便宜股[0-9]{4}", msg):
        stockNumber = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 正在為您做股票編號: {stockNumber} 便宜股健診...'))
        stockName = stockprice.get_stock_name(stockNumber)
        if stockName == "no": line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤"))
        else:
            content = Msg_diagnose.cheap_stock_menu(stockNumber, stockName)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match('ETF技術面[0-9]', msg):
        stockNumber = msg.strip("ETF技術面")
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 分析ETF編號: {stockNumber}的股價中...'))
        content = Msg_Template.etf_tec_analysis(stockNumber)
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match('ETF基本面[0-9]', msg):
        stockNumber = msg.strip("ETF基本面")
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 分析ETF編號: {stockNumber}的股價中...'))
        content = Msg_Template.etf_fundation_analysis(stockNumber)
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("MACD[0-9]", msg):
        stockNumber = msg[4:]
        content = Msg_Template.macd_msg
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 分析ETF編號: {stockNumber} MACD指標...'))
        line_bot_api.push_message(uid, TextSendMessage(content))
        MACD_imgurl = Technical_Analysis.MACD_pic(stockNumber, msg)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=MACD_imgurl, preview_image_url=MACD_imgurl))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match('RSI[0-9]', msg):
        stockNumber = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 將給您編號{stockNumber} RSI指標...'))
        RSI_imgurl = Technical_Analysis_test.stock_RSI(stockNumber)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=RSI_imgurl, preview_image_url=RSI_imgurl))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match("BBAND[0-9]", msg):
        stockNumber = msg[5:]
        content = Msg_Template.bband_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 將給您編號{stockNumber} BBand指標...'))
        BBANDS_imgurl = Technical_Analysis.BBANDS_pic(stockNumber, msg)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=BBANDS_imgurl, preview_image_url=BBANDS_imgurl))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match('F[0-9]', msg):
        stockNumber = msg[1:]
        line_bot_api.push_message(uid, TextSendMessage(f'稍等一下, 將給您編號: {tockNumber}三大法人買賣資訊...'))
        content = Institutional_Investors.institutional_investors(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage(content))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match('刪除[0-9]{4}',msg): # 刪除存在資料庫裡面的股票
        content = mongodb.delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('清空股票',msg): # 刪除存在資料庫裡面的股票
        content = mongodb.delete_my_allstock( user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('我的股票',msg): # 股票清單報價
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 股票查詢中...'))
        content = mongodb.show_my_stock(uid, user_name, msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('股票清單',msg): # 查詢股票篩選條件清單
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 股票查詢中...'))
        content = mongodb.show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("P[0-9]{4}",msg):
        stockNumber = msg[1:]
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 股價走勢繪製中...'))
        trend_imgurl = stockprice.stock_trend(stockNumber, msg)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=trend_imgurl, preview_image_url=trend_imgurl))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match("K[0-9]{4}",msg):
        stockNumber = msg[1:]
        content = Msg_Template.kchart_msg + "\n" +Msg_Template.kd_msg
        line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, K線圖繪製中...'))
        k_imgurl = kchart.draw_kchart(stockNumber)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=k_imgurl, preview_image_url=k_imgurl))
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    #--------------------------- 籌碼面分析 ---------------------------------------
    elif re.match('股票籌碼面[0-9]',msg):
        targetStock = msg[5:]
        line_bot_api.push_message(uid, TextSendMessage(f'分析{targetStock} 籌碼面中，稍等一下。'))
        # 推撥籌碼面分析圖
        imgurl2 = Institutional_Investors.institutional_investors_pic(targetStock)
        if imgurl2 == "股票代碼錯誤!": 
            line_bot_api.push_message(uid, TextSendMessage("股票代碼錯誤!"))
            return 0
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=imgurl2, preview_image_url=imgurl2))
        btn_msg = Msg_Template.stock_reply_other(targetStock)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    # 個股年收益率
    elif re.match('收益率[0-9]',msg):
        targetStock = msg[3:]
        line_bot_api.push_message(uid, TextSendMessage(f'分析{targetStock}中，稍等一下。'))
        imgurl2 = stockprice.show_return(targetStock, msg)# 收益率分析圖
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=imgurl2, preview_image_url=imgurl2))
        btn_msg = Msg_Template.stock_reply_other(targetStock)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match('外幣[A-Z]{3}',msg):
        currency = msg[2:5] # 外幣代號
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": 
            content = "無可支援的外幣"
            line_bot_api.push_message(uid, TextSendMessage(content))
        else:
            line_bot_api.push_message(uid, TextSendMessage(f'您要查詢的外幣是: {currency_name}'))
            text_message = EXRate.showCurrency(currency)
            content = Msg_Exrate.realtime_currency(text_message, currency)
            line_bot_api.push_message(uid, content)
        return 0
    elif re.match("CT[A-Z]{3}", msg):
        currency = msg[2:5] # 外幣代號
        if EXRate.getCurrencyName(currency) == "無可支援的外幣":
            line_bot_api.push_message(uid, TextSendMessage('無可支援的外幣'))
            return 0
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 將會給您匯率走勢圖'))
        cash_imgurl = EXRate.cash_exrate_sixMonth(currency)            
        if cash_imgurl == "現金匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('現金匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImageSendMessage(original_content_url=cash_imgurl, preview_image_url=cash_imgurl))
        
        spot_imgurl = EXRate.spot_exrate_sixMonth(currency)
        if spot_imgurl == "即期匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('即期匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImageSendMessage(original_content_url=spot_imgurl, preview_image_url=spot_imgurl))
        btn_msg = Msg_Exrate.realtime_currency_other(currency)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    # 匯率查詢
    # 匯率換算(台銀)
    elif re.match("買入外幣[A-Z]{3}[0-9]", msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        else:
            line_bot_api.push_message(uid, TextSendMessage("正在為您做外幣換算......"))
            content = EXRate.exchange_currency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("賣出外幣[A-Z]{3}[0-9]", msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        else:
            line_bot_api.push_message(uid, TextSendMessage("正在為您做外幣換算......"))
            content = EXRate.exchange_currency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))                   
        return 0
    elif re.match('新增外幣[A-Z]{3}', msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援的外幣": content = "無可支援的外幣"
        elif re.match('新增外幣[A-Z]{3}[<>][0-9]', msg):
            content = mongodb.write_my_currency(uid , user_name, currency, msg[7:8], msg[8:])
        else:
            content = mongodb.write_my_currency(uid , user_name, currency, "未設定", "未設定")
        
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('刪除外幣[A-Z]{3}', msg):
        content = mongodb.delete_my_currency(user_name, msg[4:7])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("換匯[A-Z]{3}/[A-Z{3}]", msg):
        line_bot_api.push_message(uid,TextSendMessage("將為您做外匯計算....."))
        content = EXRate.getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('清空外幣', msg):
        content = mongodb.delete_my_allcurrency(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('我的外幣', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 匯率查詢中...'))
        content = mongodb.show_my_currency(uid, user_name)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match('外幣清單',msg): # 查詢外幣篩選條件
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 外幣查詢中...'))
        content = mongodb.show_currency_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    elif re.match("每週回顧", msg):
        line_bot_api.push_message(uid, TextSendMessage("我們將給您最新的周回顧"))
        line_bot_api.push_message(uid, Msg_News.weekly_finance_news())
        return 0
    elif re.match('N[0-9]{4}', msg): # 個股新聞
        stockNumber = msg[1:5]
        content = Msg_News.single_stock(stockNumber)
        line_bot_api.push_message(uid, TextSendMessage(f'即將給您代號{stockNumber} 個股新聞'))
        line_bot_api.push_message(uid, content)
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    elif re.match("N外匯[A-Z]{3}", msg):
        currency = msg[3:6]
        line_bot_api.push_message(uid, TextSendMessage("將給您最新外匯消息"))
        line_bot_api.push_message(uid, Msg_News.exrate_news())
        btn_msg = Msg_Exrate.realtime_currency_other(currency)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    else:
        line_bot_api.push_message(uid, TextSendMessage('尚未讀取到'))
        return 0
    
if __name__ == "__main__":
    app.run(debug=True)

