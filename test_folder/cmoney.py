import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
appid = "20191201171605733" # 個人AppID
appsecret = "34005150141b11ea8ddf000c29cc8594" # 應用程式密鑰
token_url = "https://owl.cmoney.com.tw/OwlApi/auth"

token_params = "appId=" + appid + "&appSecret=" + appsecret

token_headers = {'content-type': "application/x-www-form-urlencoded"}

token_res = requests.request("POST", token_url, headers=token_headers, data=token_params)    
if (token_res.status_code == 200):   
    token_data = json.loads(token_res.text) 
    token = token_data.get("token")  # 取得你的token
    print ("token ok>>>" + token) 
else:                      
    print("取得token連線錯誤!" + str(token_res.status_code))

# ==================================
# 個股關鍵財務比率
def PE_ratio(pid):
    data_url = "https://owl.cmoney.com.tw/OwlApi/api/v2/json/"
    data_headers = {"authorization": "Bearer " + token}
    data_res = requests.get(data_url+pid, headers = data_headers)
    jData = json.loads(data_res.text)
    pd_data = pd.DataFrame(jData["Data"] ,columns=jData["Title"])
    pd_data.set_index("股票代號", inplace=True)
    # free = pd.to_numeric(pd_data["自由現金流量(千)"], errors='coerce') > 0
    # candidate = pd_data[free]["股票名稱"]
    # print(jData["Title"])
    # print(jData["Data"][0])
    # print(candidate)
    print(pd_data)

pid = "FDC-14834b" # 產品ID
PE_ratio(pid)

# ==================================
# 個股關鍵財務比率
# def         
