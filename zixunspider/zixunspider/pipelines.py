# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.pipelines.files import FilesPipeline
import scrapy
from urllib.parse import urlparse
from os.path import basename,dirname,join



class ZixunspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class MysqlTwistedPipline_zhulong(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
                    insert into zixun_new(title,create_date,content,tags,url,crawl_time,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
        cursor.execute(insert_sql, (item["title"], item["create_date"], item["content"], item["tags"], item["url"], item["crawl_time"],item['url_object_id']))



class MysqlTwistedPipline_archina(object):
    # 用于archinaSpider提取
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)



class MysqlTwistedPipline_jianzhushibao(object):

    #用于  MysqlTwistedPipline_zhulong 的提取
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
                    insert into jianzhushibao(title,create_date,author,content,from_web,url,crawl_time,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
        cursor.execute(insert_sql,(item["title"], item["create_date"], item["author"], item["content"],  item["from_web"],  item["url"],  item["crawl_time"], item["url_object_id"]))



class MysqlTwistedPipline_hangjian(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
                    insert into hangjian(title,create_date,author,content,from_web,url,crawl_time,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
        cursor.execute(insert_sql, (item["title"], item["create_date"], item['author'],item["content"], item["from_web"], item["url"], item["crawl_time"],item['url_object_id']))



class MysqlTwistedPipline_jianzhuxueyuan(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
                    insert into jianzhuxueyuan(title,create_date,tags,content,url,crawl_time,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
        cursor.execute(insert_sql, (item["title"], item["create_date"], item['tags'],item["content"], item["url"], item["crawl_time"],item['url_object_id']))




class MysqlTwistedPipline5(object):
    #建筑学院规范的Pipline
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
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
                    insert into jianzhu_xueyuan(file_title,file_num,file_size,file_type,file_url,one_class,two_class)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
        cursor.execute(insert_sql, (item["file_title"],item["file_num"],item["file_size"],item["file_type"],item["file_url"],item["one_class"],item["two_class"]))



class myfilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for url in item["file_url"]:
            yield scrapy.Request(url)


    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        # path = os.path.join('D:\\result',''.join(request.url+'.zip'))
        # return path


        path = urlparse(request.url).path

        return join(basename(dirname(path)), basename(path))
