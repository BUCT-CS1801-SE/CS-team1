from bs4 import BeautifulSoup
import requests
import pymysql
import urllib.request
import urllib.parse
import unicodedata
import time
import sys
import re

#反扒机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
urlHead = "https://baike.baidu.com/item/"

# 连接数据库
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'wtt0621',
    db = 'spider',
    charset='utf8'
)

#语句解析器
cur = conn.cursor()

cur.execute("select collectName from collect")
res = cur.fetchall()

# 获取藏品列表
lists = []
for i in res:
    lists.append(i[0])

for collect in lists:
    web  = requests.get(urlHead + collect, headers = headers)
    doc = BeautifulSoup(web.text, 'html.parser')
    # 简介
    div = doc.find('div', attrs={'class':'lemma-summary'})
    if div is None:continue
    content = div.get_text()
    content = re.sub("(\[\d+(\-\d+)?\])|(\n)", "", content)
    # print(content)
    time.sleep(0.5)
    # 存入数据库
    sql = "update collect set introduce=\'" + content + "\' where collectName=\'" + collect + "\'"
    try:
        cur.execute(sql)
        conn.commit()
        print("Yes!")
    except:
        print("Error!:"+sql)
        conn.rollback()

cur.close()
conn.close()