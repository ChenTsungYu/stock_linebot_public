"""
module modified from: https://github.com/bradlucas/get-yahoo-quotes-python/blob/master/get-yahoo-quotes.py

ref: http://blog.bradlucas.com/posts/2017-06-03-yahoo-finance-quote-download-python/
"""

import re
import requests
import datetime
import time
import pandas as pd
from io import StringIO


def split_crumb_store(v):
    return v.split(':')[2].strip('"')


def find_crumb_store(lines):
    # Looking for
    # ,"CrumbStore":{"crumb":"9q.A4D1c.b9
    for l in lines:
        if re.findall(r'CrumbStore', l):
            return l
    print("Did not find CrumbStore")


def get_cookie_value(r):
    return {'B': r.cookies['B']}


def get_page_data(symbol):
    url = "https://finance.yahoo.com/quote/{}/?p={}".format(symbol, symbol)
    r = requests.get(url)
    cookie = get_cookie_value(r)

    # Code to replace possible \u002F value
    # ,"CrumbStore":{"crumb":"FWP\u002F5EFll3U"
    # FWP\u002F5EFll3U
    lines = r.content.decode('unicode-escape').strip().replace('}', '\n')
    return cookie, lines.split('\n')


def get_cookie_crumb(symbol):
    cookie, lines = get_page_data(symbol)
    crumb = split_crumb_store(find_crumb_store(lines))
    return cookie, crumb


def get_data(symbol, start_date, end_date, cookie, crumb):
    filename = '{}.csv'.format(symbol)
    url = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&crumb={}".format(symbol, start_date, end_date, crumb)
    response = requests.get(url, cookies=cookie)
    with open (filename, 'wb') as handle:
        for block in response.iter_content(1024):
            handle.write(block)


def get_now_epoch():
    # @see https://www.linuxquestions.org/questions/programming-9/python-datetime-to-epoch-4175520007/#post5244109
    return int(time.time())


def download_quotes(symbol):
    start_date = 0
    end_date = get_now_epoch()
    cookie, crumb = get_cookie_crumb(symbol)
    get_data(symbol, start_date, end_date, cookie, crumb)


def download_quotes_dataframe(symbol):
    start_date = 0
    end_date = get_now_epoch()
    cookie, crumb = get_cookie_crumb(symbol)
    return get_dataframe(symbol, start_date, end_date, cookie, crumb)


def get_quotes(symbol, start_date, end_date=None):
    start_date = start_date.timestamp()
    if end_date:
        end_date = end_date.timestamp()
    else:
        end_date = get_now_epoch()
    cookie, crumb = get_cookie_crumb(symbol)
    return get_dataframe(symbol, start_date, end_date, cookie, crumb)
    

def get_dataframe(symbol, start_date, end_date, cookie, crumb):
    filename = '%s.csv' % (symbol)
    url = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1={:0.0f}&period2={:0.0f}&interval=1d&events=history&crumb={}".format(symbol, start_date, end_date, crumb)
    response = requests.get(url, cookies=cookie)
    df = pd.read_csv(StringIO(response.text), header=0, skiprows=[1], index_col=0, parse_dates=True)
    return df


if __name__=="__main__":
    start_date = datetime.datetime(2017, 1, 12)
    end_date = datetime.datetime(2018, 1, 5)
    df = get_quotes('TSLA', start_date, end_date)
    print(df.head())
    print(df.tail())