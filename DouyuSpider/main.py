__author__ = "purelove"
__date__ = "2018/2/14 下午5:56"


from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "douyu"])
# execute(["scrapy", "crawl", "home_money"])
# execute(["scrapy", "crawl", "zhihu"])