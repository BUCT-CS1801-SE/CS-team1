from bs4 import BeautifulSoup
import requests
import pymysql
import sys
import urllib.request
import urllib.parse
import unicodedata


#反扒机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url = "http://www.chnmuseum.cn/"

# 展览信息
web = requests.get(url, headers=headers)
doc = BeautifulSoup(web.text, 'html.parser')

print(web.text)