# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['www.douyu.com/directory/all']
    start_urls = ['https://www.douyu.com/1229']

    def parse(self, response):
        title =response.xpath('//*[@id="anchor-info"]/div[2]/div[1]/h2/text()').extract()[0]
        title =response.css('.entry-header h1::text').extract()[0]
        pass

