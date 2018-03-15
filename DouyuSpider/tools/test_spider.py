__author__ = "purelove"
__date__ = "2018/2/22 下午10:04"

import requests
from scrapy.selector import Selector
def spider_douyu():
    headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
    for i in range(10):
        re = ("http://www.baidu.com/{0}/{1}".format(i,i+1))
        print(re)
    # print(re.text)
    # print(re.status_code)
    # sel = Selector(text=re.text)
    # all_trs =sel.css("")

spider_douyu()