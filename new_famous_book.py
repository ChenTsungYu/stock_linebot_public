''' 
博客來新書榜、暢銷榜
'''
import requests
from bs4 import BeautifulSoup

def getnewbook():
    url='https://www.books.com.tw/web/sys_newtopb/books/02/?loc=P_0002_003'
    html=requests.get(url)
    html.encoding='utf-8'
    headers={'user-agent':'Mozilla/5.0'}
    sp=BeautifulSoup(html.text,'lxml')
    m=sp.select('.mod_a')[0].select('.item')
    rank = 0
    title_list = []
    url_list = []
    for i in m:
        rank += 1
        title = i.find_all('h4')[0].text
        if len(title) > 20: title = title[0:20]
        title_list.append(title)
        url_list.append(i.select('a')[0]['href'])
        if rank == 3:
            return title_list, url_list

def getfamousbook():
    url='https://www.books.com.tw/web/sys_saletopb/books/02/?loc=P_0002_003'
    html=requests.get(url)
    html.encoding='utf-8'
    headers={'user-agent':'Mozilla/5.0'}
    sp=BeautifulSoup(html.text,'lxml')
    m=sp.select('.mod_a')[0].select('.item')
    rank = 0
    title_list = []
    url_list = []
    for i in m:
        rank += 1
        title = i.find_all('h4')[0].text
        if len(title) > 20: title = title[0:20]
        title_list.append(title)
        url_list.append(i.select('a')[0]['href'])
        if rank == 3:
            return title_list, url_list
