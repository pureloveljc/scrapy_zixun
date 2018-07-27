# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi

class YujianspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class RedisPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms) #small problems

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        #处理异步插入的异常
        print (failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        #根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql = """
                    insert into beauty_data(name,sex,birth,xingzuo,shengao,
                    tizhong,hukou,jiguan,mobile,wexin,
                    hunyin,qq,xueli,gudingdianhua,shouru,xuexiao,danwei,jiaoyou,xingqu,
                    caiyi)
                    VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
            """
        cursor.execute(insert_sql, (item["name"],item["sex"],item["birth"],item["xingzuo"],item["shengao"],
                                    item["tizhong"],item["hukou"],item["jiguan"],item["mobile"],item["wexin"],item["hunyin"],item["qq"],item["xueli"],
                                    item["gudingdianhua"],item["shouru"],item["xuexiao"],item["danwei"],item["jiaoyou"],item["xingqu"],item["caiyi"]))



