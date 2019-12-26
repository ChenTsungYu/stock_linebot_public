from linebot.models import *
greeting_msg = '每個人的投資風格與適合的投資商品不盡相同，在開始使用本理財機器人之前，可以先做以下問卷了解自己適合的投資商品跟分析方法呦~'
Q1_msg = '你手邊有多少閒置資金(能100%投入市場的錢)?\n'
Q1_option1 = '1. 50萬以下\n'
Q1_option2 = '2. 50萬 – 500萬\n'
Q1_option3 = '3. 500萬以上'
Q1 = Q1_msg + Q1_option1 + Q1_option2 +Q1_option3
Q2_msg = '這筆錢你能承受多大虧損?\n'
Q2_option1 =  '1. 不能虧損超過10%\n'
Q2_option2 = '2. 不能虧損超過50%\n'
Q2_option3 = '3. 不能虧損超過100%\n'
Q2_option4 = '4. 虧損超過100%也可以'
Q2 = Q2_msg + Q2_option1+ Q2_option2+ Q2_option3+ Q2_option4
Q3_msg = '假設你有200萬，以下的獲利速度「最慢」可以接受哪一個?\n'
Q3_option1 = '1. 一年賺到200萬\n'
Q3_option2 = '2. 三年賺到200萬\n'
Q3_option3 = '3. 七年賺到200萬\n'
Q3_option4 = '4. 十五年賺到200萬'
Q3 = Q3_msg + Q3_option1+ Q3_option2+ Q3_option3+ Q3_option4
Q4_msg = '以下哪一個敘述，比較符合你獲利和風險的要求?\n'
Q4_option1 = '1. 虧損50%以上都還可以承受，最好能每年獲利100%以上\n'
Q4_option2 = '2. 最多有可能虧損10%的情況，每年希望至少15%以上的獲利\n'
Q4_option3 = '3. 賺多少無所謂，但不能有任何虧損!'
Q4 = Q4_msg + Q4_option1+ Q4_option2+ Q4_option3
Q5_msg = '假設你選擇高風險、高獲利的方法，你覺得賺多少錢才夠?\n'
Q5_option1 = '1. 賺到5000萬可以慢慢收手才夠下半輩子花\n'
Q5_option2 = '2. 賺到1000萬可以慢慢收手'
Q5 = Q5_msg + Q5_option1+ Q5_option2
Q6_msg = '你目前能投入多少時間學投資?\n'
Q6_option1 = '1. 可以一年看30本書、每天研究 2小時以上\n'
Q6_option2 = '2. 每周投入 5~10小時研究\n'
Q6_option3 = '3. 我工作或事業很忙，沒空學投資'
Q6 = Q6_msg + Q6_option1+ Q6_option2+ Q6_option3
Q7_msg = '以下哪個比較符合你的現狀?\n'
Q7_option1 = '1. 我每天都可以看盤，也很喜歡看盤做出判斷\n'
Q7_option2 = '2. 我喜歡透過價格或籌碼數據統計、價格圖表做出分析\n'
Q7_option3 = '3. 我喜歡透過基本面的數據分析\n'
Q7_option4 = '4. 我不想要太多研究分析，我只要一個簡單又保證能賺錢的方法'
Q7 = Q7_msg + Q7_option1+ Q7_option2+ Q7_option3 + Q7_option4
Q8_msg = '以下哪一個敘述比較符合你的個性?\n'
Q8_option1 = '1. 在好公司股價便宜時買進，太貴的時候賣出，賺取中間價差\n'
Q8_option2 = '2. 經過精心研究，找到幾間可能成長10倍以上的好公司，重押它們'
Q8 = Q8_msg + Q8_option1+ Q8_option2
type_A = 'https://imgur.com/Rmg1cBk.png'
type_B = 'https://i.imgur.com/0uRNHO0.png'
type_C = 'https://imgur.com/EVa0m3n.png'
type_D = 'https://i.imgur.com/519Bhta.png'
type_E = 'https://i.imgur.com/44Krykt.png'
type_F = 'https://imgur.com/gxvIwtA.png'
type_G = 'https://imgur.com/QJ8Fjxn.png'
type_H = 'https://imgur.com/mTubAqV.png'
type_I = 'https://imgur.com/kaTkE5b.png'
type_J = 'https://imgur.com/9us18wJ.png'

def Q1_menu():
    flex_message = FlexSendMessage(
        alt_text="Q1_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/4aAMQqU.png",
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
                            "text": "題目一",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
                        }
                        ]
                        # ,
                        # "action": {
                        #     "type": "datetimepicker",
                        #     "label": "action",
                        #     "data": "hello",
                        #     "mode": "date"
                        # }
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
                                "label": "1-1",
                                "text": "Q2"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "1-2",
                                "text": "Q3"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "1-3",
                                "text": "Q4"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message

def Q2_menu():
    flex_message = FlexSendMessage(
        alt_text="Q2_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/tbms8tz.png",
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
                            "text": "題目二",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
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
                                "label": "2-1",
                                "text": "類型J"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "2-2",
                                "text": "Q5"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "2-3",
                            "text": "類型F"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "2-4",
                            "text": "類型G"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message


def Q3_menu():
    flex_message = FlexSendMessage(
        alt_text="Q3_menu",
            contents={
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://i.imgur.com/BaZ3GFJ.png",
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
                                    "text": "題目三",
                                    "weight": "bold",
                                    "size": "xl",
                                    "align": "center",
                                    "style": "normal",
                                    "decoration": "none"
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
                                    "label": "3-1",
                                    "text": "類型I"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                    "type": "message",
                                    "label": "3-2",
                                    "text": "Q7"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "3-3",
                                        "text": "Q6"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "3-4",
                                        "text": "類型E"
                                    }
                                }
                                ],
                                "flex": 0
                            }
            }
    )
    return flex_message

def Q4_menu():
    flex_message = FlexSendMessage(
        alt_text="Q4_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/kbhPOCo.png",
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
                            "text": "題目四",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
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
                            "label": "4-1",
                            "text": "類型G"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "4-2",
                            "text": "Q6"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "4-3",
                            "text": "類型H"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message

def Q5_menu():
    flex_message = FlexSendMessage(
        alt_text="Q5_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/kPWTulj.png",
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
                            "text": "題目五",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
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
                            "label": "5-1",
                            "text": "類型I"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "5-2",
                            "text": "Q6"
                            }
                        }
                        ],
                        "flex": 0
                    }
                }
    )
    return flex_message

def Q6_menu():
    flex_message = FlexSendMessage(
        alt_text="Q6_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/TzNo8K9.png",
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
                            "text": "題目六",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
                        }
                        ],
                        "action": {
                        "type": "datetimepicker",
                        "label": "action",
                        "data": "hello",
                        "mode": "date"
                        }
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
                            "label": "6-1",
                            "text": "Q7"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "6-2",
                            "text": "Q8"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "6-3",
                            "text": "類型E"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message

def Q7_menu():
    flex_message = FlexSendMessage(
        alt_text="Q7_menu",
            contents=
            {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/MR5mDZI.png",
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
                            "text": "題目七",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
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
                            "label": "7-1",
                            "text": "類型D"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "7-2",
                            "text": "類型C"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "7-3",
                            "text": "Q8"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "7-4",
                            "text": "類型E"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message

def Q8_menu():
    flex_message = FlexSendMessage(
        alt_text="Q8_menu",
            contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/4aAMQqU.png",
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
                            "text": "題目八",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "style": "normal",
                            "decoration": "none"
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
                            "label": "8-1",
                            "text": "類型A"
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "message",
                            "label": "8-2",
                            "text": "類型B"
                            }
                        }
                        ],
                        "flex": 0
                    }
            }
    )
    return flex_message





