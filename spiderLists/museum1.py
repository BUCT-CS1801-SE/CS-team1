from bs4 import BeautifulSoup
import requests
import pymysql
import sys
import urllib.request
import urllib.parse
import unicodedata


#反扒机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url = "https://www.dpm.org.cn/"

# 展览信息
web  = requests.get("https://gugongzhanlan.dpm.org.cn/exhibitShare/134", headers = headers)
doc = BeautifulSoup(web.text, 'html.parser')

html = doc.find('div', attrs={'class':'exInfo'})
content = html.get_text()
content = content.split('\n')

info = []

for i in content:
    if i == '':continue
    i = unicodedata.normalize('NFKD', i)
    info.append(i)

dir = {}
dir['name'] = info[0] + info[1]
dir['time'] = info[2]
dir['location'] = info[3]
dir['introducation'] = info[4]
print(dir)


collections = []
html = doc.find_all('div', attrs={'class':'tabsCon'})
for content in html:
    content = content.get_text()
    content = content.split('\n')
    for i in content:
        if i == '': continue
        collections.append(i)
print(collections)
