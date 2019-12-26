''' 
股票健檢選單、地雷股選單、成長股選單、定存股選單、便宜股選單
'''
from linebot.models import *
import filter_stock

def diagnose_menu(): # 股票健檢選單
    flex_message = FlexSendMessage(
        alt_text="股票健診清單",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://imgur.com/aw4knSO.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "fit",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "股票健檢",
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
                        "label": "排除地雷股健診",
                        "text": "排除地雷股健診"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "定存股健診",
                        "text": "定存股健診"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "成長股健診",
                        "text": "成長股健診"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "便宜股健診",
                        "text": "便宜股健診"
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

def mine_stock_menu(stockNumebr, stockName): # 地雷股健檢
    content = filter_stock.mine_stock(stockNumebr)
    pass_list = content[0]
    ans = content[1]
    count = content[2]
    color_list = content[3]
    flex_message = FlexSendMessage(
        alt_text="地雷股健診",
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "排除地雷股健診完整報告",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/cDCNgaK.png",
                        "size": "xl",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "地雷股健診利用 6 項與現金流、資產週轉相關指標，鑑定公司是否有虛增獲利，假帳灌水的風險。"+ stockName +"在這 6 個指標中，通過了其中"+ count +"個 (" + ans + ")合格條件。",
                        "color": "#666666",
                        "wrap": True,
                        "margin": "xxl",
                        "size": "xs"
                    },
                    {
                        "type": "separator",
                        "margin": "none"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[0],
                                "color": color_list[0],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "1. 自由現金流入近五年有三年大於 0",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[1],
                                "color": color_list[1],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "2. 自由現金流入近五年平均大於 0",
                                "color": "#111111",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[2],
                                "color": color_list[2],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "3. 營業現金流入對淨利比近五年有三年大於 100%",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[3],
                                "color": color_list[3],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "4. 營業現金流入對淨利比近五年平均大於 100%",
                                "color": "#111111",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[4],
                                "color": color_list[4],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "5. 應收帳款週轉天數小於等於去年同期數據",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[5],
                                "color": color_list[5],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "6. 存貨週轉天數小於等於去年同期數據",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
    )
    return flex_message

def growth_stock_menu(stockNumebr, stockName): # 成長股健診
    content = filter_stock.growth_stock(stockNumebr)
    pass_list = content[0]
    ans = content[1]
    count = content[2]
    color_list = content[3]
    flex_message = FlexSendMessage(
        alt_text="成長股健診",
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "成長股健診完整報告",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/e6Hhqrm.png",
                        "size": "xl",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "成長股健診利用 5 項和損益成長相關的指標，鑑定公司短期業績成長表現好壞。"+ stockName +"在這 5 個指標中，通過了其中" + count +"個 ("+ ans +") 合格條件。",
                        "color": "#666666",
                        "wrap": True,
                        "margin": "xxl",
                        "size": "xs"
                    },
                    {
                        "type": "separator",
                        "margin": "none"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[0],
                                "color": color_list[0],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "1. 月營收 YOY 連續三個月大於 0",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[1],
                                "color": color_list[1],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "2. 近一季毛利年增率大於 0",
                                "color": "#111111",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[2],
                                "color": color_list[2],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "3. 近一季營業利益年增率大於 0",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[3],
                                "color": color_list[3],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "4. 近一季稅前淨利年增率大於 0",
                                "color": "#111111",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[4],
                                "color": color_list[4],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "5. 近一季稅後淨利年增率大於 0",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
                }
    )
    return flex_message

def fixed_deposit_stock_menu(stockNumebr, stockName): # 定存股健診
    content = filter_stock.dinchun(stockNumebr)
    pass_list = content[0]
    ans = content[1]
    count = content[2]
    color_list = content[3]
    flex_message = FlexSendMessage(
        alt_text="定存股健診",
            contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "定存股健診完整報告",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "image",
                    "url": "https://i.imgur.com/DEsuu4Z.png",
                    "size": "xl",
                    "margin": "xxl"
                },
                {
                    "type": "text",
                    "text": "定存股健診利用 5 項和股息、殖利率相關的指標，鑑定公司是否適合作為定存股投資。"+ stockName +"在這 5 個指標中，通過了其中" + count + " 個 ("+ ans +") 合格條件。",
                    "color": "#666666",
                    "wrap": True,
                    "margin": "xxl",
                    "size": "xs"
                },
                {
                    "type": "separator",
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": pass_list[0],
                            "color": color_list[0],
                            "size": "xs"
                        },
                        {
                            "type": "text",
                            "text": "1.近一年股息殖利率大於 6 %",
                            "color": "#111111",
                            "flex": 4,
                            "wrap": True,
                            "size": "xs"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": pass_list[1],
                            "color": color_list[1],
                            "size": "xs"
                        },
                        {
                            "type": "text",
                            "text": "2.近五年平均股息殖利率大於 6 %",
                            "color": "#111111",
                            "wrap": True,
                            "flex": 4,
                            "size": "xs"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": pass_list[2],
                            "color": color_list[2],
                            "size": "xs"
                        },
                        {
                            "type": "text",
                            "text": "3.連續五年都有發股息",
                            "color": "#111111",
                            "flex": 4,
                            "wrap": True,
                            "size": "xs"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": pass_list[3],
                            "color": color_list[3],
                            "size": "xs"
                        },
                        {
                            "type": "text",
                            "text": "4.股息發放率五年內有三年大於 50 %",
                            "color": "#111111",
                            "wrap": True,
                            "flex": 4,
                            "size": "xs"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": pass_list[4],
                            "color": color_list[4],
                            "size": "xs"
                        },
                        {
                            "type": "text",
                            "text": "5.股息發放率五年平均大於 50%",
                            "flex": 4,
                            "wrap": True,
                            "size": "xs"
                        }
                        ]
                    }
                    ]
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
        }
    )
    return flex_message

def cheap_stock_menu(stockNumebr, stockName): # 便宜股健診
    content = filter_stock.cheap_stock(stockNumebr)
    pass_list = content[0]
    ans = content[1]
    count = content[2]
    color_list = content[3]
    flex_message = FlexSendMessage(
        alt_text="便宜股健診",
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "便宜股健診完整報告",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/6h18eQ9.png",
                        "size": "xl",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "價值股健診利用3個判斷股價是否低估的指標，鑑定公司股價是否相對便宜。"+ stockName +"在這3個檢查中，通過了其中"+ count +"個 (" + ans + ")合格條件。",
                        "color": "#666666",
                        "wrap": True,
                        "margin": "xxl",
                        "size": "xs"
                    },
                    {
                        "type": "separator",
                        "margin": "none"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[0],
                                "color": color_list[0],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "1. 本益比<12",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[1],
                                "color": color_list[1],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "2. 股價淨值比 < 18",
                                "color": "#111111",
                                "wrap": True,
                                "flex": 4,
                                "size": "xs"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": pass_list[2],
                                "color": color_list[2],
                                "size": "xs"
                            },
                            {
                                "type": "text",
                                "text": "3. 累計合併營收成長 > 15",
                                "color": "#111111",
                                "flex": 4,
                                "wrap": True,
                                "size": "xs"
                            }
                            ]
                        }
                        
                        ]
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
        }
    )
    return flex_message