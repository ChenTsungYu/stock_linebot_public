'''
爬取stockfeel網站的文章

文本被隱藏的問題可看: https://blog.csdn.net/boystray/article/details/81065461
此檔已經可用
'''
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.stockfeel.com.tw/lemonfinance/?info=industry&order=DESC&now=1&tag=info-topic&class=infowall')
# browser.execute_script("window.open()""
# browser.page_source
# print(browser.page_source)
# content = browser.page_source
inf_title = browser.find_elements_by_css_selector(".inf-title")
content = ""
for i in range(len(inf_title)):
   inf_img = browser.find_elements_by_css_selector('.inf-img')[i]
   img_text = inf_img.get_attribute('style')
   # print(img_text)
   filter_text = img_text.split(' ')
   # print(filter_text[1])
   filter_url = filter_text[1]
   filter_image_url = re.sub("url\W{2}", "",filter_url)
   filter_image_url = filter_image_url[:-3]
   content += inf_title[i].get_attribute('textContent') + '\n' + filter_image_url + '\n'

print(content)

# print(filter_image_url)

browser.close()
# print(browser.find_element_by_css_selector(".inf-title").is_displayed()) # 檢查定位的元素是否被隱藏
# print(inf_title.get_attribute('textContent')) # 因為定位的元素被隱藏，無法直接從.text獲得文本內容
# browser.close()