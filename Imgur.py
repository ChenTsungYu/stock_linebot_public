'''
Upload pics
'''
import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = 'Your imgur client id'
client_secret = 'Your imgur client secret'
album_id = 'Your imgur album id'
access_token = 'Your imgur access token'
refresh_token = 'Your imgur refresh token'

def showImgur(fileName):
        # connect imgur
        client= ImgurClient(client_id, client_secret, access_token, refresh_token)
    
        # params
        config = {
            'album': album_id, # album name
            'name': fileName, # pics name
            'title': fileName, # pics title
            'description': str(datetime.date.today())
            }
        
        # Upload file
        try:
            print("[log:INFO]Uploading image... ")
            imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
            #string to dict
            print("[log:INFO]Done upload. ")
        except :
            # if faild to upload
            imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
            print("[log:ERROR]Unable upload ! ")
            
        
        return imgurl
