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

# 爬取信息并处理

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
        
        # info为信息字典，从中获——‘馆藏精品’，‘开放时间’，‘联系电话’
        # 对应数据库字段，‘collectionInfo’，‘openTime’，‘telephone’
        # 采用update语句更新信息
        # update museum set telephone='***', collectionInfo='***',openTime='***'
        # where museumName = '***'

        sql = "update museum set "
        sta = ""

        if '官方电话' in info:
            sta += "telephone='" + info['官方电话'] + "'"
        if '馆藏精品' in info:
            if len(sta) > 0:
                sta += ","
            sta += "collectionInfo='" + info['馆藏精品'] + "'"
        if '开放时间' in info:
            if len(sta) > 0:
                sta += ","
            sta += "openTime='" + info['开放时间'] + "'"
        if sta == "": continue
        sql += sta + " where museumName='" + museum + "'"
        try:
            cur.execute(sql)
            conn.commit()
            print("yes!_" + museum)
        except:
            print("error:" + sql)
            conn.rollback()

        # # 数据筛选：
        # if '馆藏精品' in info:
        #     print(museum + "的馆藏精品：" + info['馆藏精品'])
        #     filew.write(museum + "的馆藏精品：" + info['馆藏精品'] + '\n')
        
        # # 写入文件
        # filew.write(str(info) + "\n")

        # 访问时延，防止高速访问ip被封
        time.sleep(0.5)

# 关闭文件流
file.close()
filew.close()
# 关闭数据库
cur.close()
conn.close()