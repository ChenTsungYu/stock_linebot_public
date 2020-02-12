'''
emoji編碼列表：
https://apps.timwhitlock.info/emoji/tables/unicode#block-6c-other-additional-symbols
'''
import requests
from bs4 import BeautifulSoup
happy= u'\U0001F604' # emoji 需以unicode進行編碼 (源碼: U+1F604) 
emoji_list = [u'\U0001F4D5', u'\U0001F606']
# 個股新聞
def get_single_stock_news(stockNumber):
    url =  requests.get('https://tw.stock.yahoo.com/q/h?s=' + stockNumber)
    sp = BeautifulSoup(url.text, "html.parser")
    table = sp.find_all('table')[2]
    title_list = []
    url_list = []
    for i in range(1, 6): # 前五則消息
        trs = table.find_all('a')[i]
        title = trs.text
        if len(title) > 20: title = title[0:20] 
        title_list.append(title)
        url_list.append(trs.get("href"))
    return title_list, url_list
# 鉅亨網新聞(外幣匯率新聞)
def anue_forex_news():
    url = requests.get('https://news.cnyes.com/news/cat/forex')
    sp1 = BeautifulSoup(url.text, "html.parser")
    title_list = []
    url_list = []
    for i in range(0, 5):
        table1 = sp1.find_all('a', class_='_1Zdp')[i]
        url_list.append(table1.get('href'))
        title = table1.get('title')
        if len(title) > 20: title = title[0:20]
        title_list.append(title)
        # content += title1 +  '\n'  +'https://news.cnyes.com' +herf1 + '\n ------ \n'
    return title_list, url_list

#鉅亨網新聞(頭條新聞)
def anue_headline_news():
    url2 = requests.get('https://news.cnyes.com/news/cat/headline')
    sp2 = BeautifulSoup(url2.text, "html.parser")
    content = ''
    for i in range(0,5):
        table2 = sp2.find_all('a',class_='_1Zdp')[i]
        herf2 = table2.get('href')
        title2 = table2.get('title')
        content += title2 +  '\n'  +'https://news.cnyes.com' +herf2 + '\n ------ \n'
    return content

#每周財經大事新聞
def weekly_news():
    url3 = requests.get('https://pocketmoney.tw/articles/')
    sp3 = BeautifulSoup(url3.text, "html.parser")
    get_img = sp3.find_all('img', class_="wp-post-image")[0]
    table3 = sp3.find_all('a',class_='post-thumb')[0]
    herf3 = table3.get('href')
    img3 = get_img.get("src")
    return img3, herf3
# print(weekly_news())

# 台股盤勢(yahoo)
def twStock_news():
    url = requests.get('https://tw.stock.yahoo.com/news_list/url/d/e/N2.html')
    sp = BeautifulSoup(url.text, "html.parser")
    content = ""
    for i in range(1, 10,2):
        table = sp.find_all("a", class_='mbody')[i]
        herf = table.get("href")
        content += emoji_list[0] + herf + '\n \n' 
    return content

# 股市重大要聞(yahoo)
def important_news():
    url1 = requests.get('https://tw.stock.yahoo.com/news_list/url/d/e/N1.html')
    sp1 = BeautifulSoup(url1.text, "html.parser")
    content = ""
    for i in range(1, 10,2):
        table1 = sp1.find_all("a", class_='mbody')[i]
        herf1 = table1.get("href")
        content += happy + herf1 + '\n \n'
    return content
# 鉅亨網新聞(台灣政經新聞)
def anue_news():
    news_url = requests.get('https://news.cnyes.com/news/cat/tw_macro')
    sp2 = BeautifulSoup(news_url.text, "html.parser")
    content = ""
    # print(sp)
    for i in range(0, 5):
        table2 = sp2.find_all('a', class_='_1Zdp')[i]
        herf2 = table2.get('href')
        title2 = table2.get('title')
        content += title2 +  '\n' +herf2 + '\n ------ \n'
        # print(title2)
    return content
