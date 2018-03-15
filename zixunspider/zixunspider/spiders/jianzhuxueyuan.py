# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import  parse
from utils.common import get_md5
import datetime
from zixunspider.settings import USER_AGENT
from zixunspider.items import jianzhuxueyuan_Item



class JianzhuxueyuanSpider(scrapy.Spider):
    name = 'jianzhuxueyuan'
    allowed_domains = ['www.archcollege.com/cat/news']
    start_urls = ['http://www.archcollege.com/cat/news/']
    start_url ='http://www.archcollege.com/cat/news?t=a&cname=news&orderby=&page={0}'
    page = 1
    headers = {
        'User-Agent': USER_AGENT
    }

    # all_urls = []
    # for x in range(1, 280):  # [1~279]
    #     url ='http://www.archcollege.com/cat/news?t=a&cname=news&orderby=&page={0}'.format(x)
    #     all_urls.append(url)

    def parse(self, response):
        next_flag = False
        post_nodes =response.css('.lay_1172.course_list.type_list .cf_clear .cat-post-item a')
        for post_node in post_nodes:
            post_url = post_node.css('::attr(href)').extract_first("")
            next_flag =True
            yield Request(url=parse.urljoin(response.url, post_url), dont_filter=True, headers=self.headers, callback = self.parse_detail)

        #下一页的url解析
        if next_flag:
            self.page+=1
            yield Request(url=self.start_url.format(self.page), headers=self.headers, dont_filter=True, callback=self.parse)


    def parse_detail(self,response):
        item =jianzhuxueyuan_Item()
        title = response.css(".atcl_head h1::text").extract_first("")
        create_date =response.css(".cf_clear.hd_br span::text").extract_first("").strip() #需要用正则修改
        tags =response.css(".cf_clear.hd_br a::text").extract()
        tags = ','.join(tags)
        content = response.css(".atcl_extend").extract()
        url =response.url
        crawl_time = datetime.datetime.now()
        url_object_id = get_md5(response.url)
        item['title']= title
        item['create_date'] =create_date
        item['tags'] = tags
        item['content']= content
        item['crawl_time'] = crawl_time
        item['url']= url
        item['url_object_id']= url_object_id
        yield item
