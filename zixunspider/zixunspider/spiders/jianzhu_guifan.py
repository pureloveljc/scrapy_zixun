# -*- coding: utf-8 -*-
import scrapy
import json
import re
from PuchengSpider.items import jianzhuItem

class JianzhuspiderSpider(scrapy.Spider):
    name = 'jianzhuSpider'
    allowed_domains = ['www.archcollege.com/']
    start_urls = ['http://www.archcollege.com/interface.php?m=menuthird&a=getpost&cid=43&page=1']
    start_jianzhu_url='http://www.archcollege.com/interface.php?m=menuthird&a=getpost&cid=43&page={0}'
    page = 1
    start_jianzhu_urls= [start_jianzhu_url+str(page)]
    # headers = {
    #     "HOST": "www.archcollege.com/",
    #     "Referer": "http://www.archcollege.com",
    #     'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en"
    # }
    def parse(self, response):
        next_flag = False
        xuexyuan_json = json.loads(response.text)
        for xueyuan in xuexyuan_json["result"]["menulist"]:
            jianzhu_item = jianzhuItem()
            jianzhu_item["file_title"]= xueyuan["file_title"]
            jianzhu_item["file_num"]= xueyuan["file_num"]
            jianzhu_item["file_size"]= xueyuan["file_size"]
            jianzhu_item["file_type"] = "null"
            jianzhu_item["file_url"] = [xueyuan["file_url"]]
            jianzhu_item["one_class"] = "其它资源"
            jianzhu_item["two_class"] = "法律法规"
            next_flag = True
            yield jianzhu_item
        #for i in range(1,3):
        if next_flag:
            self.page +=1
            yield scrapy.Request(self.start_jianzhu_url.format(self.page),dont_filter=True, callback=self.parse)
        #yield scrapy.Request(self. start_jianzhu_urls[0], dont_filter=True,callback=self.parse)

    def parse_detail(self,response):
       pass

