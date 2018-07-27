# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import redis
import re
from urllib import parse
from YujianSpider.items import YujianspiderItem
from scrapy_redis.spiders import RedisSpider
from scrapy.utils.project import get_project_settings
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from twisted.internet.error import ConnectionRefusedError

class YujianSpider(RedisSpider):
    name = 'yujian'
    redis_key = "yujian_tasks"
    # str1='QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    allowed_domains = ['hn.sfywh.com']
    # str3 ='http://hn.sfywh.com/w/wedding/sousuobianhao?sousuo={}'
    # list2 = xunhuan(str1)
    # start_urls = ["http://hn.sfywh.com/w/wedding/sousuobianhao?sousuo=" + str(x) for x in list2]
    start_urls = [
        'http://hn.sfywh.com/w/wedding/sousuobianhao?sousuo=Cfm4',

    ]
    base_urls = 'http://hn.sfywh.com/w/wedding/sousuobianhao?sousuo={}'

    custom_settings = {
        # SCHEDULER_QUEUE_KEY = '{}%(spider)s:requests'.format(parse(.)),
        # 'START_URLS_KEY': '%(name)s:start_urls',
        'distributed': True,  # 分布式：默认是True
        'RETRY_TIMES': 0,
        'DOWNLOAD_TIMEOUT': 1,
        'CONCURRENT_REQUESTS': '30',
        'REDIRECT_ENABLED': True,
        'HTTPERROR_ALLOWED_CODES': [302, 304,],
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        'DOWNLOAD_DELAY': 0.1,
    }

    def make_requests_from_url(self, url):
        """ This method is deprecated. """
        print(url)
        return scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def errback(self, failure):
        self.logger.error(repr(failure))
        if failure.check(HttpError) and (failure.value.response.status == 500):
            # request = failure.request
            # id = request.meta.get('id')
            # self.logger.info('err_id:{}'.format(id))
            # self.server.rpush('err_id', id)
            pass

    def parse(self, response):
        url = re.findall(".*window.location.href='(.*)'", response.text)[0]
        print(url)
        res_url = 'http://hn.sfywh.com'+url
        yield Request(url=res_url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        article_item = YujianspiderItem()
        name = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[1]/text()").extract_first()
        sex = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[2]/text()").extract_first()
        birth = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[3]/text()").extract_first()
        xingzuo = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[4]/text()").extract_first()
        shengao = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[5]/text()").extract_first()
        tizhong = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[6]/text()").extract_first()
        hukou = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[7]/text()").extract_first()
        jiguan = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[8]/text()").extract_first()
        try:
            mobile = re.findall('.*/(\d*)', response.url)[0]
        except:
            mobile = ''
        wexin = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[10]/text()").extract_first()
        hunyin = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[11]/text()").extract_first()
        qq = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[12]/text()").extract_first()
        xueli = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[13]/text()").extract_first()
        gudingdianhua = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[14]/text()").extract_first()
        shouru = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[15]/text()").extract_first()
        xuexiao = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[16]/text()").extract_first()
        danwei = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[17]/text()").extract_first()
        jiaoyou = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[18]/text()").extract_first()
        xingqu = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[19]/text()").extract_first()
        caiyi = response.xpath("//*[@class='wrap']/div[2]/div[1]/div[1]/div[20]/text()").extract_first()

        article_item['name'] = name
        article_item['sex'] = sex
        article_item['birth'] = birth
        article_item['xingzuo'] = xingzuo
        article_item['shengao'] = shengao
        article_item['tizhong'] = tizhong
        article_item['hukou'] = hukou
        article_item['jiguan'] = jiguan
        article_item['mobile'] = mobile
        article_item['wexin'] = wexin
        article_item['hunyin'] = hunyin
        article_item['qq'] = qq
        article_item['xueli'] = xueli
        article_item['gudingdianhua'] = gudingdianhua
        article_item['shouru'] = shouru
        article_item['xuexiao'] = xuexiao
        article_item['jiaoyou'] = jiaoyou
        article_item['danwei'] = danwei
        article_item['xingqu'] = xingqu
        article_item['caiyi'] = caiyi

        yield article_item


if __name__ == '__main__':
    # mongo_cli = pymongo.MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
    import redis
    from scrapy.crawler import CrawlerProcess
    import scrapy

    redis_key = "yujian_tasks"

    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
    # conn = redis.Redis(connection_pool=pool)
    # pip = conn.pipeline()
    # _id_list = conn.lrange('queue:bianhao', 1, 1700000)
    # base_url ='http://hn.sfywh.com/w/wedding/sousuobianhao?sousuo={}'
    # for num in _id_list:
    #     # num = '18994585568'
    #     # num = item.get("_id")
    #     # taskInfo = eval(num)
    #     bs = str(num, encoding="utf8")
    #     pip.rpush('yujian_tasks', base_url.format(str(bs)))
    #     print(bs)
    #
    # pip.execute()

    #
    # process = CrawlerProcess()
    process = CrawlerProcess(get_project_settings())
    process.crawl(YujianSpider)
    process.start()