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

#解析数据
cur.execute("select * from museum")

result = cur.fetchall()

print(result)

cur.close()
conn.close()