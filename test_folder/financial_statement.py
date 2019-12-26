'''
此檔在測試階段

'''
from FinMind.Data import Load
import requests
import pandas as pd
import datetime
url = 'http://finmindapi.servebeer.com/api/data'
list_url = 'http://finmindapi.servebeer.com/api/datalist'
translate_url = 'http://finmindapi.servebeer.com/api/translation'

# '''----------------FinancialStatements----------------'''
form_data = {'dataset':'FinancialStatements',
  	   'stock_id':'2330',
  	   'date':'2016-01-01'}
res = requests.post(
        url,verify = True,
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data = Load.transpose(data)
# print(data)
# data = data[['EPS', 'CostOfGoodsSold']]
# data =  data[['EPS']]

# '''----------------TaiwanStockStockDividend----------------'''
# form_data = {'dataset':'TaiwanStockStockDividend',
#              'stock_id':'2317',
#              'date':'2018-01-01'}
# res = requests.post(
#         url,verify = True,
#         data = form_data)

# temp = res.json()
# data = pd.DataFrame(temp['data'])
# data.head()
# -----------
# print(data.head(10)) 
# ------------------------
# date = str( datetime.datetime.now().date() - datetime.timedelta(30) )
# date2 = str( datetime.datetime.now().date() - datetime.timedelta(200) )
date3 = str( datetime.datetime.now().date() - datetime.timedelta(400) )
# #---------------------------------------------------------------
print('load TaiwanStockInfo')
TaiwanStockInfo = Load.FinData(dataset = 'TaiwanStockInfo')
print( TaiwanStockInfo[:9010] )
_index = 9010
print('load 財報 FinancialStatements {} '.format(TaiwanStockInfo.loc[2331,'stock_id']))
TaiwanStockFinancialStatements = Load.FinData(
        dataset = 'FinancialStatements',
        select = TaiwanStockInfo.loc[9010,'stock_id'],
        date = date3)
print( TaiwanStockFinancialStatements[:-1] )
