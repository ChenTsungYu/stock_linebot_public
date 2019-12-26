from linebot.models import *
import new_famous_book
# from linebot.models import TextSendMessage, FlexSendMessage, QuickReplyButton, QuickReply, MessageAction,TemplateSendMessage,ImageCarouselColumn, ImageCarouselTemplate, TextMessage
emoji = u'\U0001F538'
emoji_sub = u'\U0001F539'
emoji_idea = u'\U0001F4A1'
emoji_heart = u'\U0001F497'
emoji_thumb = u'\U0001F44D'
#=============================================
# 手機下方選單回應的訊息
menu_stock_msg = "歡迎使用股票查詢功能 輸入關鍵指令，如:「 #2002 」等股票代碼，即可獲得該股票的資訊唷!"+emoji_heart+\
"\n若輸入關鍵指令，如: 「比較2330/2002/2317」，即可一次比較多檔股票哦！"+ emoji_thumb
menu_fin_msg = "請輸入「快樂學理財」或「股票教學」、「外匯教學」或「問卷分析」，可獲得更多理財小知識哦!"+emoji_idea
menu_exrate_msg = "請輸入「外匯列表」可獲得最新外匯相關訊息，或輸入「外幣USD」可獲得美元相關訊息哦! USD可換成您要查詢的外幣代碼;若想進行國際貨幣間的換算，例如輸入「換匯usd/twd/100」即可了解100美金兌換台幣的總額哦!"+emoji_heart
menu_mylist_msg = "請輸入「我的股票」可以查詢個人清單裡的股票即時價格; 輸入「我的外幣」可查詢個人清單裡的外匯即時價格哦! "+emoji_heart
menu_etf_msg = "歡迎使用ETF查詢功能，輸入關鍵指令，如：#0050等證券代碼，即可獲得該ETF的資訊唷！"+emoji_heart
#=============================================

#=============================================
# 其他教學(與查詢的訊息一同送出)
etf_msg = emoji + "指數股票型基金，以股市前50家最大的上市公司為買進對向，投資的核心理念是以較低廉的費用買進，隨著50家大型績優企業成長而賺進長期貼近企業成長率的報酬。"
kchart_msg = emoji + "每一根K線都由四個價格組成：開盤價、最高價、最低價、收盤價。如果收盤價比開盤價高，會畫出陽線(紅K)，反之，如果收盤價比開盤價低，就會畫出陰線(綠K)。"
macd_msg = emoji + "MACD是對長期(MACD)與短期(DIF)的移動平均線，加以雙重平滑處理，用來判斷買賣股票的時機與訊號。當快線向上突破慢線/柱線由負轉正時，即為買進訊號；當快線向下跌破慢線/柱線由正轉負時，即為賣出訊號。"
kd_msg = emoji + 'KD指標取9天內的最高和最低，來反應股價整體的動能。當KD指標的K值由下往上突破D值，建議買進；當KD指標的K值由上往下跌破D值時，建議賣出。\n'\
+ emoji +'KD指標>80以上為"高檔超買"，KD<20以下為"低檔超賣"，一旦KD值到達了上述的超買區或超跌區連續三天，即為KD鈍化。\n\n' \
+emoji_sub+'當股票高檔鈍化時，表示非常的強勢，通常會再漲的機會就會變得非常高。\n'\
+emoji_sub+'當股票低檔鈍化時，表示非常的弱勢，通常會再跌的機會就會變得非常高。'
bband_msg = emoji + "布林通道:\n由布林上軌（壓力線）、布林中軌（20MA）與布林下軌（支撐線）所組成。若股價碰到上軌有可能會下跌，往中軌靠近；若股價碰到下軌可能會上漲，往中軌靠近。"
maxdd_msg = emoji + "最大回撤:\n是過去最大的資金回檔，也就是過去所經歷最大的風險。可以將MaxDD當作準備資金的參考值，也能評量一個策略在目前市場表現的狀況，若出現連續虧損已經超過歷史的 MaxDD，則要考慮這個策略在市場上是否仍然有效。"
#=============================================
def stock_info_menu(): # 股票教學
    flex_message = FlexSendMessage(
            alt_text="stock_info_menu",
            contents={
                    "type": "carousel",
                    "contents": [
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "url": "https://i.imgur.com/Aq5F8NZ.jpg"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "三大投資分析方式",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "flex": 2,
                                "action": {
                                "type": "message",
                                "label": "三大投資分析表",
                                "text": "三大投資分析表"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "基本面",
                                "text": "基本面"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "技術面",
                                "text": "技術面"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "籌碼面",
                                "text": "籌碼面"
                                }
                            }
                            ]
                        }
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "url": "https://i.imgur.com/xxI8W1N.jpg"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "投資者類型",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "flex": 2,
                                "action": {
                                "type": "message",
                                "label": "保守型投資者",
                                "text": "保守型投資者"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "激進型投資者",
                                "text": "激進型投資者"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "獨立型投資者",
                                "text": "獨立型投資者"
                                }
                            }
                            ]
                        }
                        },
                        {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "url": "https://i.imgur.com/CrdzE4z.jpg"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "專有名詞",
                                "wrap": True,
                                "weight": "bold",
                                "size": "xl",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "flex": 2,
                                "action": {
                                    "type": "message",
                                    "label": "每股盈餘(EPS)",
                                    "text": "EPS"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "多頭市場/空頭市場",
                                    "text": "多頭市場/空頭市場"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "買超/賣超",
                                    "text": "買超/賣超"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "黃金交叉/死亡交叉",
                                    "text": "黃金交叉/死亡交叉"
                                }
                            }
                            ]
                        }
                        }
                    ]
                
        }
    )
    return flex_message
# 快樂學理財
def learning_menu():
    flex_message = FlexSendMessage(
            alt_text="learning_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/r5X3sDG.png",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "fit",
                        "position": "relative",
                        "margin": "none"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "快樂學理財",
                            "weight": "bold",
                            "size": "xl",
                            "style": "normal"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "讓您輕鬆又快樂地學習理財小知識",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                }
                                ]
                            }
                            ]
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "理財youtuber推薦",
                            "text": "理財youtuber推薦"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "理財電影推薦",
                            "text": "理財電影推薦"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "理財書籍推薦",
                            "text": "理財書籍推薦"
                            }
                        },
                        {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "message",
                                "label": "理財新書榜",
                                "text": "新書榜"
                                }
                        },
                        {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "message",
                                "label": "理財暢銷榜",
                                "text": "暢銷榜"
                                }
                            },
                        {
                            "type": "spacer",
                            "size": "sm"
                        }
                        ],
                        "flex": 0
                    }          
            }
        )
    return flex_message
# 三大面向分析(教學)
def three_investment(msg):
    if msg == "基本面": return  emoji + "基本面: 研究公司內在的真實價值，可以分析產業環境、公司財報等。"
    if msg == "技術面": return  emoji + "技術面: 分析股票價格的趨勢方向，可以從股票走勢圖、K線圖等作分析。"
    if msg == "籌碼面": return  emoji + "籌碼面: 研究大戶的動向來預測股票漲跌，主要可以從三大法人的動向作分析。"
# 理財頻道
def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message
# 理財電影
def movies():
    flex_message = FlexSendMessage(
            alt_text="movies",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/iYHLmU8.jpg",
                        "aspectMode": "cover",
                        "aspectRatio": "320:213",
                        "size": "full"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "刺激1995",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center",
                            "decoration": "none"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "關鍵字：分散風險",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我看預告",
                            "uri": "https://www.youtube.com/watch?v=AAzVYa3L31M"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財電影",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/ECpL1IG.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "320:213"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "當幸福來敲門",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center",
                            "decoration": "none"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "關鍵字：永不放棄",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我看預告",
                            "uri": "https://www.youtube.com/watch?v=YjA5-WoMi-I"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財電影",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/noFIAH8.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "320:213"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "華爾街",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center",
                            "decoration": "none"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "關鍵字：內幕交易",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我看預告",
                            "uri": "https://www.youtube.com/watch?v=unpVs5xlh2M"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財電影",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message
# 理財書籍
def fin_books():
    flex_message = FlexSendMessage(
            alt_text="fin_books",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/hUWBRhe.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#DDDDDD"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "富爸爸，窮爸爸",
                            "weight": "bold",
                            "size": "md",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "暢銷二十年的經典",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.books.com.tw/products/0010720289"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財書籍",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/YYlesvX.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#DDDDDD"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "思考致富聖經",
                            "weight": "bold",
                            "size": "md",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "13個致富關鍵",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.books.com.tw/products/0010654650"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財書籍",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/uFhehyq.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#DDDDDD"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "有錢人想的和你不一樣",
                            "weight": "bold",
                            "size": "md",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "17種致富思考方式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.books.com.tw/products/0010316121?loc=P_asb_001"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財書籍",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5,
                                    "position": "relative"
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message
# 股票 quick reply(給#代碼指令)
def stock_reply(stockNumber, content_text):
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="關注", 
                                                    text="關注"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="取消關注", 
                                                    text="刪除"+stockNumber,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="P"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="K線圖", 
                                                    text="K"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="法人", 
                                                    text="F"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="三大面向分析", 
                                                    text= "三大面向分析"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text= "N"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="年收益率", 
                                                    text= "收益率" + stockNumber
                                                )
                                       ),
                                ]
                            ))
    return text_message
def stock_reply_other(stockNumber):
    content_text = "想知道更多?"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時股價", 
                                                    text="#"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="關注", 
                                                    text="關注"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="取消關注", 
                                                    text="刪除"+stockNumber,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="P"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="K線圖", 
                                                    text="K"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="法人", 
                                                    text="F"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="三大面向分析", 
                                                    text= "三大面向分析"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text= "N"+stockNumber
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="年收益率", 
                                                    text= "收益率" + stockNumber
                                                )
                                       ),
                                ]
                            ))
    return text_message

# 股票三大面向分析(查詢股價配合quick repay)
def stock_ananlysis_menu(stockNumber):
    flex_message = FlexSendMessage(
            alt_text="stock_ananlysis_menu",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/fu3yvlL.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "股票三大面向分析",
                        "weight": "bold",
                        "size": "lg"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "股票技術面",
                        "text": "股票技術面" + stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "股票基本面",
                            "text": "股票基本面" + stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "股票籌碼面" ,
                            "text": "股票籌碼面" + stockNumber
                        }
                    }
                    ],
                    "flex": 0
                }
            }
        )
    return flex_message
# 股票技術面分析
def stock_tec_analysis(stockNumber):
    flex_message = FlexSendMessage(
            alt_text="stock_tec_analysis",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/heTnHFM.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "股票技術面",
                            "weight": "bold",
                            "size": "xl",
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "股票K線圖",
                            "text": "K" + stockNumber
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "股票MACD指標",
                            "text": "MACD" + stockNumber
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "股票RSI指標",
                            "text": "RSI" + stockNumber
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "股票BBand",
                            "text": "BBAND" + stockNumber
                            }
                        }
                        ],
                        "flex": 0,
                        "margin": "none"
                    }
            }
    )
    return flex_message
#  股票基本面分析
def stock_fundation_analysis(stockNumber):
    flex_message = FlexSendMessage(
            alt_text="stock_fundation_analysis",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/0ofcn1s.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "股票基本面",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "股票償債能力",
                        "text": "償債能力"+stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "股票經營能力",
                        "text": "經營能力"+stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "股票獲利能力",
                        "text": "獲利能力"+stockNumber
                        }
                    }
                    ],
                    "flex": 0,
                    "margin": "none"
                }
            }
    )
    return flex_message
#  ETF技術面分析
def etf_tec_analysis(stockNumber):
    flex_message = FlexSendMessage(
            alt_text="etf_tec_analysis",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/heTnHFM.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ETF技術面",
                        "weight": "bold",
                        "size": "xl",
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "ETF-K線圖",
                        "text": "K"+ stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "ETF-RSI分析",
                        "text": "RSI" + stockNumber
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "ETF-BBand",
                        "text": "BBand" + stockNumber
                        }
                    }
                    ],
                    "flex": 0,
                    "margin": "none"
                }
            }
    )
    return flex_message
#  ETF基本面分析
def etf_fundation_analysis(stockNumber):
    flex_message = FlexSendMessage(
            alt_text="etf_fundation_analysis",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/0ofcn1s.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ETF基本面",
                        "weight": "bold",
                        "size": "xl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "ETF償債能力",
                            "text": "ETF償債能力"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "ETF經營能力",
                        "text": "ETF經營能力"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "ETF獲利能力",
                        "text": "ETF獲利能力"
                        }
                    }
                    ],
                    "flex": 0,
                    "margin": "none"
                }
            }
    )
    return flex_message
def industrial_artical():
    flex_message = FlexSendMessage(
            alt_text="產業分析文章",
            contents={
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/iUpVBLQ.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-meal"
                                    }
                                },
                                {
                                    "type": "image",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "url": "https://i.imgur.com/6hIzhDW.png",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-travel"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/LcOPeEu.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-5g-tw"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/Zr0VuQf.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-medical-equipment"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/vSgnovg.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-machinery"
                                    }
                                }
                                ],
                                "flex": 1
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/DIGkMmx.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-chinese-food"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/Fiz2Mr5.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-shoes"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/9YwUvbz.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-access-support"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/ry9vcg0.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-esportlaptop"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/LrrX4cI.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-autopilot"
                                    }
                                }
                                ],
                                "flex": 1
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/tBxb50Z.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-health-food"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/4tLWmhL.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-ecommerce"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/ot41BcD.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-smartgrid"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/c3uaWjv.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-onlinegame"
                                    }
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/ZXWQryT.png",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "150:98",
                                    "gravity": "center",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.stockfeel.com.tw/concept/?concept=concept-cloud-device"
                                    }
                                }
                                ],
                                "flex": 1
                            }
                            ]
                        }
                        ],
                        "paddingAll": "0px",
                        "spacing": "xxl",
                        "margin": "xxl"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "資料來源：STOCKFEEL 主題投資"
                        }
                        ]
                    }
            }
    )
    return flex_message

# 博客來理財暢銷書
def famous_books():
    content = new_famous_book.getfamousbook()
    title_list = content[0]
    url_list = content[1]
    flex_message = FlexSendMessage(
            alt_text="財暢銷書",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://imgur.com/knR6C5f.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    },
                    "position": "relative",
                    "margin": "none"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "暢銷榜",
                        "weight": "bold",
                        "size": "xl",
                        "style": "normal"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[0],
                        "uri": url_list[0]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": title_list[1],
                            "uri": url_list[1]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": title_list[2],
                            "uri": url_list[2]
                        }
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                    ],
                    "flex": 0
                }
        }
    )
    return flex_message

def new_books():
    content = new_famous_book.getnewbook()
    title_list = content[0]
    url_list = content[1]
    flex_message = FlexSendMessage(
            alt_text="博客來理財新書",
            contents=
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://imgur.com/gDtZ0YW.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "action": {
                        "type": "uri",
                        "uri": "http://linecorp.com/"
                    },
                    "position": "relative",
                    "margin": "none"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "新書榜",
                        "weight": "bold",
                        "size": "xl",
                        "style": "normal"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[0],
                        "uri": url_list[0]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[1],
                        "uri": url_list[1]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": title_list[2],
                            "uri": url_list[2]
                        }
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                    ],
                    "flex": 0
                }
            }
    )
    return flex_message

# 投資人類型
def investor_type(msg):
    content = emoji
    if msg == "保守型投資者":
        content += \
        "保守型投資者:\n適合買績優股、龍頭股，如台塑、中鋼、中華電信等，這些股票比較能在產業上維持長久的穩定經營地位，股價也較不會一夕變天，可以放長投資；\
投資本益比低、股息殖利率高的股票，如中華電信等電信類股，能穩健獲利；\
投資ETF，雖然報酬率不高，但在統計上是優於基金的。"        
    if msg == "激進型投資者":
        content += \
    "激進型投資者:\n目標是在最短的時間內使投資組合的價值達到最大。\
投資者通常都運用技術分析法，分析市場多空雙方的對比關係、\
均衡狀態等情況，並以此為依據作出預測，選擇有上升空間的股票。\
如日本大地震衍生出來的鋼鐵股、或剛上市上櫃仍在蜜月期的新股等。"
    if msg == "獨立型投資者":
        content += "獨立型投資者:\n通常掌握充足的金融投資知識，而且十分熱衷於金融投資，\
他們一般具備批判性的思維方式和強大的問題分析能力，擅長獨立作出決策，\
而且對自己的決策充滿信心。"
    
    return content
# 專有名詞
def proper_noun(msg):
    content = emoji
    if msg == "EPS":
        content += "每股盈餘(EPS):\n每股給投資者帶來的收益，是投資人判斷公司獲利能力的指標之一， \
若公司盈餘越高或股本越低，則EPS就越高。"
    if msg == "多頭市場/空頭市場":
        content += "多頭市場/空頭市場:\n"+emoji_sub+"多頭市場:\n又稱「牛市」，是市場(股價或指數)處於上升的趨勢中\
，在這時期買進股票賺錢的機會很高。\n" + emoji_sub + "空頭市場:\n又稱「熊市」，是市場(股價或指數)處於下跌的趨勢中\
，在這時期買進股票賠錢的機會很高。"
    if msg == "買超/賣超":
        content += "買超/賣超:\n" + emoji_sub + "買超:\n買進的數量或金額，超過賣出的數量或金額，若為三大法人買超，\
多被解讀為看漲率極高，但沒有絕對。\n" + emoji_sub + "賣超:\n賣出的數量或金額，超過買進的數量或金額，若為三大法人賣超，\
多被解讀為看跌率極高，但沒有絕對。"
    if msg == "黃金交叉/死亡交叉":
        content += "黃金交叉/死亡交叉:\n" + emoji_sub + "黃金交叉:\n技術指標時常以快慢線作為交易訊號，當快線由下方往上方交叉穿越慢線，\
即為黃金交叉，通常為看多、做多的買進訊號，根據訊號買進可能會賺錢。\n" + emoji_sub + \
"死亡交叉:\n技術指標時常以快慢線作為交易訊號，當快線由上方往下方跌落並交叉穿越慢線，即為死亡交叉，通常為看空、做空的賣出訊號\
，根據訊號賣出可能會賺錢，不賣可能會開始賠錢。"

    return content
# print(proper_noun("黃金交叉/死亡交叉"))


    


