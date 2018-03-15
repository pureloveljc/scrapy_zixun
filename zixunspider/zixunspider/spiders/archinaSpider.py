# -*- coding: utf-8 -*-
import scrapy
from zixunspider.settings import USER_AGENT
from zixunspider.items import archinaItemLoader,archina_Item
from datetime import datetime
from scrapy.http import Request
from utils.common import get_md5


class ArchinaspiderSpider(scrapy.Spider):
    name = 'archinaSpider'
    allowed_domains = ['architecture.archina.com']
    start_urls = ['http://architecture.archina.com/anews/']
    headers = {
        'User-Agent': USER_AGENT
    }

    def parse(self, response):
        post_urls =response.css('.all_b .pub_list ')
        for post_node in post_urls:
            post_url = post_node.css("a::attr(href)").extract_first("")
            yield Request(dont_filter=True, url=post_url, headers= self.headers, callback=self.parse_detail)
        next_urls = response.css(".text-c .a1:nth-child(14)::attr(href)").extract_first("")
        if next_urls:
            yield Request(url=next_urls, headers= self.headers, callback=self.parse)

    def parse_detail(self,response):
        item_loader = archinaItemLoader(item=archina_Item(), response=response)
        item_loader.add_css('title',".col-left h1::text") #列表第一个
        item_loader.add_xpath('create_date', '//*[@id="Article"]/h1/span/text()')
        item_loader.add_css('content',".col-left .content")
        item_loader.add_value('url',response.url)
        item_loader.add_value("crawl_time", datetime.now())
        item_loader.add_value('url_object_id', get_md5(response.url))
        ar_item = item_loader.load_item()
        yield ar_item

