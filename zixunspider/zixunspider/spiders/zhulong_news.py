# -*- coding: utf-8 -*-
import scrapy
from zixunspider.items import Zhulong_Item
from utils.common import get_md5


class ZhulongNewsSpider(scrapy.Spider):
    name = 'zhulong_news'
    allowed_domains = ['news.zhulong.com/']
    start_urls = ['http://news.zhulong.com/']
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        'X-Requested-With':'XMLHttpRequest'
    }


    def parse(self, response):
        post_urls = response.css(".res-list .list-item.clearfix .title.clearfix a::attr(href)").extract()
        all_urls = filter(lambda x:True if x.startswith("http://bbs") else False, post_urls)
        all_urls = filter(lambda x: x != "http://bbs.zhulong.com/9020_group_855/detail8281308", all_urls)
        all_urls = filter(lambda x:  x != "http://bbs.zhulong.com/9020_group_855/detail7997407",all_urls)
        all_urls_a = list(all_urls)
        for url in all_urls_a:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse_detail)


    def parse_detail(self, response):
        zhulong_item =Zhulong_Item()
        title = response.xpath('/html/body/div[5]/div[1]/div/div[1]/div[1]/div[2]/h1/text()').extract_first("").strip() #exract_first不用做异常处理
        create_date = response.xpath('/html/body/div[5]/div[1]/div/div[1]/div[1]/div[2]/p/text()').extract_first("").strip()
        #create_date1 = re.findall('(\d+.*)', create_date1)
        tags_list = response.css('.group_zl_tags a::text').extract()
        tags = ','.join(tags_list)
        content = response.css('div.zhul_xx_content').extract_first("")
        zhulong_item['title'] = title
        zhulong_item['create_date'] = create_date
        zhulong_item['tags'] = tags
        zhulong_item['content'] = content
        zhulong_item['url'] = response.url
        from datetime import datetime
        zhulong_item['crawl_time'] = datetime.now()
        zhulong_item['url_object_id']= get_md5(response.url)
        yield zhulong_item

