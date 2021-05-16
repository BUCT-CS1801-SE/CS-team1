# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import re
import copy
import pymysql
import logging
logger = logging.getLogger(__name__)
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'museumapp'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'wtt0621'  

#博物馆表
class MuseumsPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        item["introduction"]=self.process_content(item["introduction"])
        insert_sql = "INSERT INTO museum(museumID, museumName,introduction,opentime,Link,location,telephone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['museumID'], item['museumName'], item['introduction'], item['opentime'], item['Link'], item['Location'], item['telephone'])
        try:
            self.cursor.execute(insert_sql)

            # 4. 提交操作
            self.connect.commit()
        except:
            self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()      
    #处理数据的函数，根据自己情况设置
    def process_content(self,introduction):
        content=''
        for i in introduction:
            content+=i
        return content
#藏品表
class Collection75Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        #深拷贝
        asynItem = copy.deepcopy(item)
        item=asynItem
        # print(item['collectionName'])
        res = self.cursor.execute("select * from collection where collectionName = '" + item['collectionName'] + "'")
        if res == 0:
            insert_sql = "INSERT INTO collection(museumID,collectionName,collectionIntroduction,collectionImage) VALUES ('%s', '%s', '%s', '%s')" % (item['museumID'], item['collectionName'], item['collectionIntroduction'], item['collectionImage'])
            try:
                self.cursor.execute(insert_sql)

                # 4. 提交操作
                self.connect.commit()
            except:
                self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

#展览表(没有exhibitionintroduction,exhibitionTime)
class Exhibition75Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        cnt = self.cursor.execute("select * from exhibition where exhibitionTheme='"+item['exhibitionTheme']+"'")
        if cnt == 0:
            insert_sql = "INSERT INTO exhibition(museumID,exhibitionTheme,exhibition_picture) VALUES ('%s', '%s', '%s')" % (item['museumID'], item['exhibitionTheme'], item['exhibition_picture'])
            try:
                self.cursor.execute(insert_sql)

                # 4. 提交操作
                self.connect.commit()
            except:
                self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

class Exhibition76Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        #深拷贝
        asynItem = copy.deepcopy(item)
        item=asynItem
        # print(item)
        cnt = self.cursor.execute("select * from exhibition where exhibitionTheme='"+item['exhibitionTheme']+"'")
        if cnt == 0:
            insert_sql = "INSERT INTO exhibition(museumID,exhibitionTheme,exhibitionIntroduction,exhibition_picture) VALUES ('%s', '%s', '%s', '%s')" % (item['museumID'], item['exhibitionTheme'], item['exhibitionIntroduction'], item['exhibition_picture'])
            #insert_sql = "INSERT INTO exhibition(museumID,exhibitionTime,exhibitionTheme,exhibitionIntroduction,exhibition_picture) VALUES ('%s', '%s', '%s', '%s', '%s')" % (item['museumID'], item['exhibitionTime'], item['exhibitionTheme'], item['exhibitionIntroduction'], item['exhibition_picture'])
            try:
                self.cursor.execute(insert_sql)

                # 4. 提交操作
                self.connect.commit()
            except:
                self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()  


#博物馆表
class MuseumPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        insert_sql = "INSERT INTO museum(museumID, museumName,introduction,opentime,Link,location,telephone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['museumID'], item['museumName'], item['introduction'], item['opentime'], item['Link'], item['Location'], item['telephone'])
        try:
            self.cursor.execute(insert_sql)

            # 4. 提交操作
            self.connect.commit()
        except:
            self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()    


#展览表

class ExhibitionPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        cnt = self.cursor.execute("select * from exhibition where exhibitionTheme='"+item['exhibitionTheme']+"'")
        # print("select * from exhibition where exhibitionTheme='"+item['exhibitionTheme']+"'")
        # print(cnt)
        if cnt == 0:
            insert_sql = "INSERT INTO exhibition(museumID,exhibitionTheme,exhibition_picture,exhibitionIntroduction) VALUES ('%s', '%s', '%s','%s')" % (item['museumID'], item['exhibitionTheme'], item['exhibition_picture'],item['exhibitionIntroduction'])
            try:
                self.cursor.execute(insert_sql)
                # 4. 提交操作
                self.connect.commit()
            except:
                self.connect.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
   

#藏品表

class CollectionPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item is None: return
        #print(item)
        res = self.cursor.execute("select * from collection where collectionName = '" + item['collectionName'] + "'")
        if res == 0:
            insert_sql = "INSERT INTO collection(museumID,collectionName,collectionIntroduction,collectionImage) VALUES ('%s', '%s', '%s', '%s')" % (item['museumID'], item['collectionName'], item['collectionIntroduction'], item['collectionImage'])
            self.cursor.execute(insert_sql)

            # 4. 提交操作
            self.connect.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
  