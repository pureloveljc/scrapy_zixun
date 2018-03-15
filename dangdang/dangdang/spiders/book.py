# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from dangdang.items import BookItem
import json
import re


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['http://www.dangdang.com/']
    start_urls = ['http://e.dangdang.com/media/api.go?action=getPcChapterInfo&epubID=1900465429&consumeType=1&platform=3&deviceType=Android&deviceVersion=5.0.0&channelId=70000&platformSource=DDDS-P&fromPaltform=ds_android&deviceSerialNo=html5&clientVersionNo=5.8.4&token=&chapterID=2&pageIndex=0&locationIndex=3&wordSize=2&style=2&autoBuy=0&chapterIndex=']
    start_url='http://e.dangdang.com/media/api.go?action=getPcChapterInfo&epubID=1900465429&consumeType=1&platform=3&deviceType=Android&deviceVersion=5.0.0&channelId=70000&platformSource=DDDS-P&fromPaltform=ds_android&deviceSerialNo=html5&clientVersionNo=5.8.4&token=&chapterID=2&pageIndex=0&locationIndex=3&wordSize=2&style=2&autoBuy=0&chapterIndex='

    # def __init__(self):
    #     # 初始化时候，给爬虫新开一个浏览器
    #     self.browser = webdriver.Chrome(executable_path="E:\pycharmprojects\dangdang\chromedriver.exe")
    #     super(BookSpider, self).__init__()
    #     dispatcher.connect(self.spider_closed,
    #                        signals.spider_closed)  # 第二个参数是信号（spider_closed:爬虫关闭信号，信号量有很多）,第一个参数是当执行第二个参数信号时候要执行的方法
    #
    # def spider_closed(self, spider):
    #     # 当爬虫退出的时候关闭chrome
    #     print("spider closed")
    #     self.browser.quit()

    def parse(self, response):
        book_json =json.loads(response.text)
        book_item =book_json["data"]["chapterInfo"]
        p1 = "<span class=[\s\S]*?left:(\d+)px; bottom:(\d+)px;[\s\S]*?>([\s\S])<"
        pattern1 = re.compile(p1)
        matcher1 = re.findall(pattern1, book_item)
        print(matcher1)

        class Word():
            def __init__(self,left,buttom,value):
                self.left = left
                self.buttmom = buttom
                self.value =value
                pass
        for x in matcher1:
            x=Word()



