from linebot.models import FlexSendMessage
import news

def single_stock(stockNumber):
    start_url = "https://tw.stock.yahoo.com"
    content = news.get_single_stock_news(stockNumber)
    title_list = content[0]
    url_list = content[1]
    flex_message = FlexSendMessage(
            alt_text="個股新聞",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/uvrIuT9.jpg",
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
                        "text": "財金新聞",
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
                        "uri": start_url + url_list[0]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[1],
                        "uri": start_url + url_list[1]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[2],
                        "uri": start_url + url_list[2]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[3],
                        "uri": start_url + url_list[3]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[4],
                        "uri": start_url + url_list[4]
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
# 外匯新聞
def exrate_news():
    start_url = "https://news.cnyes.com"
    content = news.anue_forex_news()
    title_list = content[0]
    url_list = content[1]
    flex_message = FlexSendMessage(
            alt_text="外匯新聞",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/uvrIuT9.jpg",
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
                        "text": "外匯新聞",
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
                        "uri": start_url + url_list[0]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[1],
                        "uri": start_url + url_list[1]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[2],
                        "uri": start_url + url_list[2]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[3],
                        "uri": start_url + url_list[3]
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": title_list[4],
                        "uri": start_url + url_list[4]
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
#每周財經大事新聞
def weekly_finance_news():
    content = news.weekly_news()
    img = content[0]
    url = content[1]
    flex_message = FlexSendMessage(
            alt_text="每周財經大事新聞",
            contents={
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": img,
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "1252:837",
                        "gravity": "center",
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": url
                        }
                    }
                    ],
                    "paddingAll": "0px"
                }
                }
    )
    return flex_message

