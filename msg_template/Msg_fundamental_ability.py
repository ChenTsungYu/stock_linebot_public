from linebot.models import *
import Fundamental_Analysis
# 基本面- 經營能力
def operating_ability(stockNumber, stockName):
    content = Fundamental_Analysis.get_three_index(stockNumber)
    ITRatio = content[0]  # 存貨週轉率(次)
    ATTime = content[1] # 固定資產週轉次數
    TATTime = content[2] # 總資產週轉次數
    ARRatio = content[3] # 應收帳款週轉率(次)
    flex_message = FlexSendMessage(
            alt_text="經營能力",
            contents={
                    "type": "bubble",
                    "styles": {
                        "footer": {
                        "separator": True
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": stockName, # 替換成股票名稱
                            "weight": "bold",
                            "color": "#1DB446",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "經營能力",
                            "weight": "bold",
                            "size": "xxl",
                            "margin": "md"
                        },
                        {
                            "type": "separator",
                            "margin": "md"
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
                                    "text": "期別",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "2018",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "2017",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "2016",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
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
                                    "text": ARRatio[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(ARRatio[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ARRatio[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ARRatio[3]),
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
                                    "text": ITRatio[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(ITRatio[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ITRatio[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ITRatio[3]),
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
                                    "text": ATTime[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(ATTime[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ATTime[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ATTime[3]),
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
                                    "text": TATTime[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(TATTime[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(TATTime[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(TATTime[3]),
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

# 基本面- 償債能力
def debt_ability(stockNumber, stockName):
    content = Fundamental_Analysis.get_three_index(stockNumber)
    CurrentRatio = content[4]  # 流動比率
    QuickRatio = content[5] # 速動比率
    flex_message = FlexSendMessage(
            alt_text="償債能力",
            contents={
                "type": "bubble",
                "styles": {
                    "footer": {
                    "separator": True
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": stockName,
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "償債能力",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                "text": "期別",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "2018",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#555555",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": "2017",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#555555",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": "2016",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#555555",
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
                                "text": CurrentRatio[0],
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": str(CurrentRatio[1]),
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": str(CurrentRatio[2]),
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": str(CurrentRatio[3]),
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
                                "text": QuickRatio[0],
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": str(QuickRatio[1]),
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": str(QuickRatio[2]),
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            },
                            {
                                "type": "text",
                                "text": str(QuickRatio[3]),
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

# 基本面- 獲利能力
def profit_ability(stockNumber, stockName):
    content = Fundamental_Analysis.get_three_index(stockNumber)
    GPMargin = content[6]  # 毛利率
    CostRatio = content[7] # 成本率
    EPS = content[8] # 每股盈餘
    ROE = content[9] # 股東權益報酬率
    PMargin = content[10] # 純益率
    TATRatio = content[11] # 總資產報酬率
    flex_message = FlexSendMessage(
            alt_text="獲利能力",
            contents={
                "type": "bubble",
                "styles": {
                    "footer": {
                    "separator": True
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": stockName,
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "獲利能力",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                    "text": "期別",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "2018",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "2017",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "2016",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#555555",
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
                                    "text": GPMargin[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(GPMargin[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(GPMargin[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(GPMargin[3]),
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
                                    "text": CostRatio[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(CostRatio[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(CostRatio[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(CostRatio[3]),
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
                                    "text": EPS[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(EPS[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(EPS[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(EPS[3]),
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
                                    "text": ROE[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(ROE[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ROE[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(ROE[3]),
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
                                    "text": PMargin[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(PMargin[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(PMargin[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(PMargin[3]),
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
                                    "text": TATRatio[0],
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": str(TATRatio[1]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(TATRatio[2]),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": str(TATRatio[3]),
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
