__author__ = "purelove"
__date__ = "2018/2/14 下午5:56"

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#execute(["scrapy", "crawl", "archinaSpider"])
#execute(["scrapy", "crawl", "zhulong_news"])
#execute(["scrapy", "crawl", "jianzhushibao"])
#execute(["scrapy", "crawl", "hangjian"])
execute(["scrapy", "crawl", "jianzhuxueyuan"])