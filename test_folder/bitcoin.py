import requests
from bs4 import BeautifulSoup
import json
import pandas
import matplotlib.pyplot as plt

res = requests.get('https://www.coingecko.com/price_charts/1/twd/max.json?locale=zh-tw')
jData= json.loads(res.text)
#print(jData["stats"])

df = pandas.DataFrame(jData["stats"])
df.columns = ['datatime', 'twd']
df['datatime'] = pandas.to_datetime(df['datatime'],unit='ms')
#print(df)

df.index = df['datatime']
print(df)
df['twd'].plot(kind = 'line',figsize = (10,5))
df['twd'].rolling(window = 7).mean()
df[['twd']].plot(kind = 'line', figsize=[20,5])
df2 = df[df['datatime'] >= '2017-01-01']
df2[['twd']].plot(kind = 'line', figsize=[20,5])
plt.savefig("test.png")
