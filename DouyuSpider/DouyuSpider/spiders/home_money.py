# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from DouyuSpider.items import HouseItem
from DouyuSpider.utils.common import get_md5
from DouyuSpider.settings import USER_AGENT

class HomeMoneySpider(scrapy.Spider):
    name = 'home_money'
    allowed_domains = ['su.58.com']
    start_urls = ['http://su.58.com/chuzu/']
    headers = {
       # "HOST": "su.58.com",
       # "Referer": "http://su.58.com/",
        'User-Agent':USER_AGENT
    }
    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        3.extract_first 不需要异常处理
        """
        # if response.status == 404:
        #     self.fail_urls.append(response.url)
        #     self.crawler.stats.inc_value("failed_url")
        post_nodes = response.css(".listUl")
        for post_node in post_nodes:
            front_image = post_node.css(".img_list img::attr(lazy_src)").extract_first("")
            post_url = post_node.css(".img_list a::attr(href)").extract_first("")
            yield Request(dont_filter=True,url=post_url, meta={"front_image_url":front_image}, callback=self.parse_detail)# middle中添加随机更换user-agent,不用添加self.headers
            # 我日这个dont_filter=True 找了我三天三夜 我日
        # 提取下一页的url进行下载
        next_urls = response.css(".next::attr(href)").extract_first("")
        if next_urls:
            yield Request(url=next_urls,callback=self.parse)


    def parse_detail(self, response):
        house_item = HouseItem()
        front_image_url = response.meta.get("front_image_url", "")
        title = response.css(".c_333.f20::text").extract_first()
        house_pay = response.css(".house-pay-way.f16 b::text").extract_first()
        house_chat = response.css(".house-chat-txt::text").extract_first()
        house_addr = response.css(".addr.c_555.f14::text").extract_first()
        #house_item = HouseItem()  # 实例化item
        house_item['title'] = title
        house_item['house_pay'] = house_pay
        house_item['house_chat'] = house_chat
        house_item['house_addr'] = house_addr
        house_item['url'] = response.url
        house_item['front_image_url'] = [front_image_url]
        house_item['url_object_id'] = get_md5(response.url)
        #house_item['front_image_path'] = front_image_path
        yield house_item




