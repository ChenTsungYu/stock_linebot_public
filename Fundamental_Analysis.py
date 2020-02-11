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
