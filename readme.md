# 股票&外匯機器人
## Introduction:
使用python搭配flask框架，透過Heroku免費雲端主機串接LineBot，資料庫使用MongoDB 
## Third-party Library：
* twder(Exchange Rate)
* pymongo(Database)
* imgurpython(Imgur Cloud)
* yfinance
* talib
* Heroku
## Note:
* talib: 
目錄底下的talib套件用於技術分析，只能在本地測試，若要部署上Heroku，則需要在Heroku的環境安裝talib。
* selenium:
heroku環境需另外配置。

## 參考資源：
* [Emoji for line](https://developers.line.biz/media/messaging-api/emoji-list.pdf)
* [Emoji](https://apps.timwhitlock.info/emoji/tables/unicode)
* **注意：Emoji 需以`Unicode`的形式編碼**
* [Selenium在Heroku上的配置- 官方說明](https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/)
* [Heroku的環境安裝talib](https://elements.heroku.com/buildpacks/numrut/heroku-buildpack-python-talib)
