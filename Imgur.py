'''
上傳圖片
'''
import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = '07f1098efd49fcb'
client_secret = 'c802e2b89ad38a83341f53148a41058c65a65d42'
album_id = '817ZzND'
access_token = '0409f8c9d920da65fc8bb9c3ec5b029c4dc4869c'
refresh_token = 'dd279237af22c09c879a84105e209e13bff5e227'

def showImgur(fileName):
        # 連接imgur
        client= ImgurClient(client_id, client_secret, access_token, refresh_token)
    
        # 連接需要的參數
        config = {
            'album': album_id, # 相簿名稱
            'name': fileName, # 圖片名稱
            'title': fileName, # 圖片標題
            'description': str(datetime.date.today()) # 備註，這邊打日期時間
            }
        
        # 開始上傳檔案
        try:
            print("[log:INFO]Uploading image... ")
            imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
            #string to dict
            print("[log:INFO]Done upload. ")
        except :
            # 如果失敗回傳"失敗"這張圖
            imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
            print("[log:ERROR]Unable upload ! ")
            
        
        return imgurl
