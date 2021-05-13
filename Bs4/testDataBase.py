import pymysql
#连接数据库

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'wtt0621',
    db = 'spider',
    charset='utf8'
)

#创建游标
cur = conn.cursor()

# 读取文件

file = open("museumUrl.txt", 'r', encoding='utf-8')

list = file.readlines()

for urlName in list:
    urlName = urlName.split(' ')
    url = urlName[1]
    name = urlName[0]
    sql = 'update museum set url=\'' + url[0:-1] + '\' where museumName=\'' + name + '\''
    try:
        cur.execute(sql)
        conn.commit()
        print("yes")
    except:
        print("error:" + sql)
        conn.rollback()

file.close()
cur.close()
conn.close()