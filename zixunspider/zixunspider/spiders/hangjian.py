# -*- coding: utf-8 -*-
import scrapy
from utils.common import get_md5
import datetime
from zixunspider.items import  hangjian_Item
from scrapy.http import Request
from urllib import parse
from zixunspider.settings import USER_AGENT


class HangjianSpider(scrapy.Spider):
    name = 'hangjian'
    allowed_domains = ['bim.co188.com/info_11857/']
    start_urls = ['http://bim.co188.com/info_11857//']
    all_urls = []
    for i in range(1, 53):
        url_str = 'http://bim.co188.com/info_11857/p{0}.html'.format(i)
        all_urls.append(url_str)

    headers = {
        'User-Agent':USER_AGENT
    }
    def parse(self, response):

        """
        获取当前页面的url,并交给pare_deail
        :param response:
        :return:
        """

        post_nodes =response.css(".middle_left a")
        for post_node in post_nodes:
            post_node = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_node) ,dont_filter=True, headers=self.headers ,callback=self.parse_detail)
        # 遍历所有的url下一页并交给scrapy进行下载
        for start_url in self.all_urls:
            yield Request(url=start_url, headers=self.headers, dont_filter=True, callback=self.parse)

    def parse_detail(self,response):

        """
        爬取新闻详情页
        :param response:
        :return:
        """
        item =hangjian_Item()
        title = response.css(".zixun h1::text").extract_first("")
        create_date = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[1]/div[1]/em/text()').extract_first("")
        author =response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[1]/div[6]/span/em').extract_first("")
        from_web =response.xpath('/ html/body/div/div[2]/div[1]/div[2]/div[1]/div[5]/span/em/text()').extract_first("")
        content = response.css(".zixun").extract_first("")
        url =response.url
        crawl_time =datetime.datetime.now()
        url_object_id =get_md5(response.url)
        item['title'] = title
        item['create_date'] = create_date
        item['author'] = author
        item['from_web'] = from_web
        item['content'] = content
        item['url'] = url
        item['crawl_time'] = crawl_time
        item['url_object_id'] = url_object_id
        yield item

