import pandas as pd
import matplotlib.pyplot as plt
import Imgur

def spot_exrate_sixMonth(msg2):
    dfs = pd.read_html('https://rate.bot.com.tw/xrt/quote/l6m/JPY')
    currency = dfs[0]
    currency = currency.iloc[:, 0:6]
    # 更改欄位名稱
    currency.columns = [u'掛牌日期', u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入',  u'即期匯率-本行賣出']
    currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1] #  row 順序反轉，因原始資料是從最新開始排
    ## 即期匯率
    currency.plot(kind = 'line',x='掛牌日期', y=['即期匯率-本行買入', '即期匯率-本行賣出'])
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.savefig(msg2 + ".png")
    plt.show()
    plt.close()
    return Imgur.showImgur(msg2)
def cash_exrate_sixMonth(msg1):
    dfs = pd.read_html('https://rate.bot.com.tw/xrt/quote/l6m/JPY')
    currency = dfs[0]
    currency = currency.iloc[:, 0:6]
    # 更改欄位名稱
    currency.columns = [u'掛牌日期', u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入',  u'即期匯率-本行賣出']
    currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
    currency = currency.iloc[::-1] #  row 順序反轉，因原始資料是從最新開始排
    # 現金匯率
    currency.plot(kind = 'line',x='掛牌日期', y=['現金匯率-本行買入', '現金匯率-本行賣出'])
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.savefig(msg1 + ".png")
    plt.show()
    plt.close()
    return Imgur.showImgur(msg1)
# msg1 = '2019cash_exrate_JPY_sixMonth1'
# msg2 = '2019spot_exrate_JPY_sixMonth2'
# print('cash: ', cash_exrate_sixMonth(msg1))
# print('spot: ', spot_exrate_sixMonth(msg2))
##############################  以下為測試用

# dfs = pd.read_html('https://rate.bot.com.tw/xrt/quote/l6m/JPY')
# # print(type(dfs[0]))
# # print(len(dfs))
# # print(dfs[0])
# currency = dfs[0]
# currency = currency.iloc[:, 0:6]
# print(currency)
# currency.columns = [u'掛牌日期', u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入',  u'即期匯率-本行賣出']
# print(currency[u'幣別']) # 只取出幣別
# currency[u'幣別']
# # print(currency[u'幣別'].str.extract('\((\w+)\)'))
# currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
# # print(currency.iloc[::-1])
# currency = currency.iloc[::-1] #  row 順序反轉，因原始資料是從最新開始排
 
# currency.plot(kind = 'line',x='掛牌日期', y=['現金匯率-本行買入', '現金匯率-本行賣出'])
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.savefig("2019cash_exrate_JPY_sixMonth1.png")
# plt.show()
# plt.close() 

# currency.plot(kind = 'line',x='掛牌日期', y=['即期匯率-本行買入', '即期匯率-本行賣出'])
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.savefig("2019spot_exrate_JPY_sixMonth1.png")
# plt.show()
# plt.close()
# currency.to_csv('rate.csv')

##################################################################
# CSV版本
# df = pd.read_csv('https://rate.bot.com.tw/xrt/flcsv/0/l6m/JPY')
# print(df.head())

# df.columns = []
# df['']
# print(df.head())
# print(df.info())
# df.index = pd.to_datetime(df.index, format='%Y%m%d') # 轉換時間
# print(df.index)
# print(df.info())


# df.plot(kind = 'line', y=['匯率', '現金'])
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.savefig("2019exrate_JPY3.png")
# plt.show()