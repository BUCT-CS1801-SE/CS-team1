from bs4 import BeautifulSoup
import requests
import pymysql
import urllib.request
import urllib.parse
import unicodedata
import time
import sys

#反扒机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
urlHead = "https://baike.baidu.com/item/"

# info = {}
# key = ""
# value = ""
# fl = 1
# for table in doc.find_all('div', attrs={"class":"basic-info cmn-clearfix"}):
#     getTd = table.get_text()
#     getTd = getTd.split('\n')
#     for i in getTd:
#         if i == '' or i[0] == '[': continue
#         i = unicodedata.normalize('NFKD', i)
#         if fl % 2 == 1:
#             key = i
#         else:
#             value = i
#             info[key] = value
#         fl += 1
#     print(info['馆藏精品'])


file = open('museumName.txt', 'r')
filew = open('museumInfo.txt', 'w')
museumList = file.read()
museumList = museumList.split()

for museum in museumList:
    web  = requests.get(urlHead + museum, headers = headers)
    doc = BeautifulSoup(web.text, 'html.parser')
    for div in doc.find_all('div', attrs={'class':'basic-info cmn-clearfix'}):
        content = div.get_text()
        content = content.split('\n')
        fl = 1
        info = {}
        key = ""
        value = ""
        for i in content:
            if i == '' or i[0] == '[': continue
            i = unicodedata.normalize('NFKD', i)
            if fl % 2 == 1:
                key = i
            else:
                value = i
                info[key] = value
            fl += 1
        if '馆藏精品' in info:
            print(museum + "的馆藏精品：" + info['馆藏精品'])
            filew.write(museum + "的馆藏精品：" + info['馆藏精品'] + '\n')
        time.sleep(0.5)
