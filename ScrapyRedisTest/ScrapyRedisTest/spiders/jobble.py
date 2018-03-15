# -*- coding: utf-8 -*-
__time__ = '2018/3/15 0015'
__author__ = 'purelove'

from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    name = 'myspider'


    def parse(self, response):
        # do stuff
        pass