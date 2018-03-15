# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import re


class ZixunspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Zhulong_Item(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()


class archinaItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()


def remove_create(value):
    date = value.replace("   来源：","").strip()
    return date


class archina_Item(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(remove_create)
    )
    content =scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
                    insert into archina_new(title,create_date,content,url,crawl_time,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s)
            """
        params = (self["title"], self["create_date"], self["content"], self["url"],self["crawl_time"],self["url_object_id"])
        return insert_sql, params


def remove_title(value):
    title = value.strip()
    return title


# def get_author(value):
#     value.
#     author = value.srtip()
#     return author

class jianzhuItemLoader(ItemLoader):
    #自定义itemloader

    default_output_processor = TakeFirst()


class jianzhushibao_Item(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    from_web = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()

    # def get_insert_sql(self):
    #     insert_sql = """
    #                 insert into jianzhushibao(title,create_date,author,content,from_web,url,crawl_time,url_object_id)
    #                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    #         """

        # title = self["title"]
        # title = title.extract_first("")
        # resultone= self["create_date"]
        # create_date = re.findall('.*?(\d{4}[-年]\d{1,2}[-月]\d{1,2}[-日])', resultone)
        # resultwo = self["author"]
        # author = re.findall('.*?(作者.*)', resultwo)
        # content = self["content"].extract_first("")
        # from_web = self["from_web"].extract_first("")
        # url=self["url"].extract_first("")
        # crawl_time=self["crawl_time"].extract_first("")
        # url_object_id= self["url_object_id"]
        # params = (title, create_date, author, content, from_web, url,crawl_time,url_object_id)
        #params = (self["title"], self["create_date"], self["author"], self["content"], self["from_web"], self["url"], self["crawl_time"], self["url_object_id"])
        #return insert_sql, params


class hangjian_Item(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    from_web = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()


class jianzhuxueyuan_Item(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()




class jianzhuItem(scrapy.Item):
    #建筑规范的Item
    file_title =scrapy.Field()
    file_num = scrapy.Field()
    file_size=scrapy.Field()
    file_type=scrapy.Field()
    file_url=scrapy.Field()
    one_class =scrapy.Field()
    two_class =scrapy.Field()



class filedownItem(scrapy.Item):
    file_url =scrapy.Field()