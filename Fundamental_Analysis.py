'''
基本面三大能力評估所需的值: 經營能力、獲利能力、償債能力
'''
import requests
import pandas as pd
import numpy as np
import datetime

import pandas
import numpy as np

def get_three_index(stockNumber):
    url='http://jsjustweb.jihsun.com.tw/z/zc/zcr/zcra/zcra_'+stockNumber+'.djhtm'
    url1='https://www.cnyes.com/twstock/finratio2/'+stockNumber+'.htm'

    basic=pandas.read_html(url)
    basic1=pandas.read_html(url1)
    # 能力名稱
    ability = [basic[2][1][45].strip('指標單位：% / 次 / 天'), basic[2][1][58].strip('指標單位：%'), basic1[0]['項目'][19]]
    terms = ["2018年", "2017年", "2016年"] # 期別
    ARRatio = [] # 應收帳款週轉次
    ITRatio = [] # 存貨週轉率(次)
    ATTime = []  # 固定資產週轉次數
    TATTime = []  # 總資產週轉次數
    CurrentRatio = []# 流動比率
    QuickRatio = [] # 速動比率
    GPMargin = ["毛利率"] # 毛利率
    CostRatio = ["成本率"] # 成本率
    EPS = ["每股盈餘"] # 每股盈餘
    ROE = ["股東權益報酬率"] # 股東權益報酬率
    PMargin = ["純益率"] # 純益率
    TATRatio = ["總資產報酬率"] # 總資產報酬率
    for i in range(0, 4):
        ARRatio.append(basic[2][i][50])
        ITRatio.append(basic[2][i][52])
        ATTime.append(basic[2][i][54])
        TATTime.append(basic[2][i][49])
        CurrentRatio.append(basic[2][i][63])
        QuickRatio.append(basic[2][i][64])
    for year in terms:
        GPMargin.append(str(basic1[0][year][19]))
        CostRatio.append(str(basic1[0][year][20]))
        EPS.append(str(basic1[0][year][29]))
        ROE.append(str(basic1[0][year][34]))
        PMargin.append(str(basic1[0][year][28]))
        TATRatio.append(str(basic1[0][year][33]))
    return ITRatio , ATTime, TATTime, ARRatio,CurrentRatio, QuickRatio, GPMargin, CostRatio, EPS, ROE, PMargin, TATRatio
 
# stockNumber='2330'
# print(get_three_index(stockNumber))

# def financial_statement(type='資產負債表'):
    
#     # 決定要抓什麼時候的報表
#     today = datetime.date.today() # 今天的時間
#     year=today.year # 預設年是今年
#     year =year-1911 # 必須要是民國年
    
#     if type == '綜合損益表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04'
#     elif type == '資產負債表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
#     elif type == '營益分析表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
#     else:
#         print('type does not match')
        
#     for season in range(4,0,-1):
#         r = requests.post(url, {
#             'encodeURIComponent':1,
#             'step':1,
#             'firstin':1,
#             'off':1,
#             'TYPEK':'sii',
#             'year':str(year),
#             'season':str(season),
#         })
        
#         r.encoding = 'utf8'
        
#         if not('查詢無資料' in r.text):
#             break
        
# ### 如果四季都查完，還是'查無資料'，代表是在年初，要抓前一年第四季 ###    
#     if '查詢無資料' in r.text:
#         r = requests.post(url, {
#             'encodeURIComponent':1,
#             'step':1,
#             'firstin':1,
#             'off':1,
#             'TYPEK':'sii',
#             'year':str(year-1),
#             'season':4,
#         })
        
#         r.encoding = 'utf8'
        
#     if '查詢無資料' in r.text:
#         r = requests.post(url, {
#             'encodeURIComponent':1,
#             'step':1,
#             'firstin':1,
#             'off':1,
#             'TYPEK':'sii',
#             'year':str(year-1),
#             'season':3,
#         })
        
#         r.encoding = 'utf8'
#     dfs = pd.read_html(r.text)
    
    
#     for i, df in enumerate(dfs):
#         df.columns = df.iloc[0] # 把欄位名稱丟進去
#         dfs[i] = df.iloc[1:] # 
        
#     df = pd.concat(dfs).applymap(lambda x: x if x != '--' else np.nan)
#     df = df[df['公司代號'] != '公司代號']
#     df = df[~df['公司代號'].isnull()]
    
#     return df

# # 毛利率篩選
# def gpm():
#     df=financial_statement(type='營益分析表')
#     return '\n'.join(df[pd.to_numeric(df['毛利率(%)(營業毛利)/(營業收入)'])>70]['公司代號'])

# # 每股淨值篩選
# def pbr():
#     df=financial_statement(type='資產負債表')
#     return '\n'.join(df[pd.to_numeric(df['每股參考淨值'])>10]['公司代號'])

# # 每股盈餘篩選
# def eps():
#     df=financial_statement(type='綜合損益表')
#     return '\n'.join(df[pd.to_numeric(df['基本每股盈餘（元）'])>2]['公司代號'])

# print(eps())