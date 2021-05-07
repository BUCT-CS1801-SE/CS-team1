from bs4 import BeautifulSoup
import requests
import pymysql



html = requests.get("https://www.aicesu.cn/museum/")

doc = BeautifulSoup(html.text, "html.parser")

# #结果文件
file1 = open("museum.txt", 'w')
file2 = open("museumName.txt", 'w')

#连接数据库

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'wtt0621',
    db = 'spider',
    charset='utf8'
)
#语句解析器
cur = conn.cursor()

id = 1
for table in doc.find_all('tr'):
    txt = table.get_text()
    info = txt.split()
    if len(info) >= 3 and info[2] == "一级":
        file1.write(str(info) + "\n")
        file2.write(info[0] + "\n")
        # insert into museum values(id, name, type, rank, open, location)
        # sen = "insert into museum values('" + str(id) + "'"
        # for i in info:
        #     if i == "是" or i == "否":
        #         if i == "是": i = '1'
        #         else : i = '0'
        #     sen = sen + ',\'' + i + '\''
        # sen = sen + ')'
        # id += 1
        # try:
        #     cur.execute(sen)
        #     conn.commit()
        # except:
        #     print("error:" + sen)
        #     conn.rollback()

file2.close()
cur.close()
conn.close()


