# from linebot.models import *
from linebot.models import TextSendMessage, FlexSendMessage, QuickReplyButton, QuickReply, MessageAction
from EXRate import get_currency_list
emoji = u'\U0001F538'
#=====================================
# 教學
Exrate_msg = emoji+"外幣是一種商品，簡單來說，就是能用多少本國貨幣買到各國外幣，是一相對的概念\n"\
+emoji+"為何會漲跌？\n總體經濟＋政策干預 → 一國貨幣貶值，錢會往幣值相對較高（或被看好）的國家跑"

#=====================================

def realtime_menu():
    currency = get_currency_list()
    flex_message = FlexSendMessage(
        alt_text="台銀即期外匯",
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "LINE BOT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "即期外匯",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "台灣匯率",
                        "size": "sm",
                        "color": "#aaaaaa",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "美金USD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[0],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "港幣HKD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[1],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "英鎊GBP",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[2],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "澳幣AUD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[3],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "加拿大幣CAD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[4],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "新加坡幣SGD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[5],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "瑞士法郎CHF",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[6],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end" 
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "日圓JPY",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[7],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "南非幣ZAR",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[8],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "瑞典幣SEK",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[9],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "紐元NZD",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[10],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "泰幣THB",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[11],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "菲國比索PHP",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[12],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "印尼盾IDR",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[13],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "歐元EUR",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[14],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "韓元KRW",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[15],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "越南盾VND",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[16],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "馬來幣MYR",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[17],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "人民幣CNY",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$"+ currency[18],
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]  
                        }
                        ]
                    }
                    ]
                }
            }   
    )
    return flex_message

def realtime_currency(content, currency):
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message
def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="外幣"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message