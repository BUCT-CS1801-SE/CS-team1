import re
import pymysql
from bs4 import BeautifulSoup
import requests

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

cur.execute('select museumName, collectionInfo from museum')
res = cur.fetchall()

dir = {}

for info in res:
    if info[1] is None: continue
    museum = info[0]
    collect = info[1]
    collect = re.split(',|，|、|;', collect)
    for i in collect:
        if i[-1] == '等': i = i[0:-1]
        dir[i] = museum

for key, val in dir.items():
    sql = "insert into collect(collectName, museum) values(\'" + key + "\',\'" + val + "\')"
    try:
        cur.execute(sql)
        conn.commit()
        print("yes!")
    except:
        print("error!:" + sql)
        conn.rollback()

cur.close()
conn.close()