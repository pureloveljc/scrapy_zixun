import scrapy
from zixunspider.settings import USER_AGENT
from zixunspider.items import jianzhushibao_Item
from datetime import datetime
from scrapy.http import Request
from urllib import  parse
from utils.common import get_md5
import datetime

class JianzhushibaoSpider(scrapy.Spider):
    name = 'jianzhushibao'
    allowed_domains = ['www.jzsbs.com/design/']
    start_urls = ['http://www.jzsbs.com/design/']
    headers = {
        'User-Agent': USER_AGENT
    }
    all_urls = [   'http://jzsbs.com/design/index_2.html',
                  'http://jzsbs.com/design/index_3.html',
                  'http://jzsbs.com/design/index_4.html',
                  'http://jzsbs.com/design/index_5.html',
                  'http://jzsbs.com/design/index_6.html',
                  'http://jzsbs.com/design/index_7.html',
                  'http://jzsbs.com/design/index_8.html',
                  'http://jzsbs.com/design/index_9.html',
                  'http://jzsbs.com/design/index_10.html',
                  'http://jzsbs.com/design/index_11.html',
                  'http://jzsbs.com/design/index_12.html',
                  'http://jzsbs.com/design/index_13.html',
                  'http://jzsbs.com/design/index_14.html',
                  'http://jzsbs.com/design/index_15.html',
                  'http://jzsbs.com/design/index_16.html',
                  ]

    def parse(self, response):
        post_nodes = response.css('.lay_1172.course_list.type_list .cf_clear a')
        for post_node in post_nodes:
            post_url = post_node.css('::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), dont_filter=True, headers=self.headers, callback = self.parse_detail)
        for start_url in self.all_urls:
            yield Request(url=start_url, headers=self.headers,dont_filter=True, callback=self.parse)


    def parse_detail(self, response):
        import re
        item = jianzhushibao_Item()
        title = response.css('.content-left h1::text').extract_first()
        resultone= response.css('.content-left-wenzhang-time::text').extract()
        create_date = re.findall('.*?(\d{4}[-年]\d{1,2}[-月]\d{1,2}[-日])', resultone[0])

        if create_date:
            create_date = create_date[0].replace('年', '-')
            create_date = create_date.replace('月', '-')
            create_date = create_date.replace('日', '')
            print(create_date)
            create_date = datetime.datetime.strptime(create_date, "%Y-%m-%d").date()
        else:
            create_date =''

        resultwo = response.css('.content-left-wenzhang-time::text').extract()
        str4 = "".join(resultwo)
        author = re.findall('.*?(作者.*)', str4)
        if author:
            author = author[0]
        else:
            author = ''
        from_web = response.css('.content-source a::text').extract_first()
        if from_web is None:
            from_web =response.css('.content-source::text').extract_first()
        content = response.css('.content-left').extract_first()
        pass
        item['title'] = title
        item['create_date'] = create_date
        item['author'] = author
        item['url'] = response.url
        item['from_web'] = from_web
        item['content'] = content
        item['crawl_time'] = datetime.datetime.now()
        item['url_object_id'] = get_md5(response.url)
        yield item


