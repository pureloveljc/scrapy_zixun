# -*- coding: utf-8 -*-

# Scrapy settings for DouyuSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
BOT_NAME = 'DouyuSpider'

SPIDER_MODULES = ['DouyuSpider.spiders']
NEWSPIDER_MODULE = 'DouyuSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DouyuSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10 #10下载延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True #禁用

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DouyuSpider.middlewares.DouyuspiderSpiderMiddleware': 543,
#}
HTTP_PROXY = 'http://127.0.0.1:8123'
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'DouyuSpider.middlewares.RandomUserAgentMiddlware':400,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   #'DouyuSpider.middlewares.ProxyMiddleware':410,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DouyuSpider.pipelines.DouyuspiderPipeline': 300,
   #'scrapy.pipelines.images.ImagesPipeline': 1, #自动下载图片的Piple
   #'scrapy.pipelines.files.FilesPipeline': 2,
   #'DouyuSpider.pipelines.homePipele':1,
    #'DouyuSpider.pipelines.MysqlPipeline':1,
   'DouyuSpider.pipelines.MysqlTwistedPipeline': 1,

}

IMAGES_URLS_FIELD = 'front_image_url'
project_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(project_dir, 'images')


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True  #启用扩展
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5 #初始下载延迟
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60 #在高延迟情况下最大的下载延迟
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
RANDOM_UA_TYPE = "random"
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "home_scrapy"
MYSQL_USER = "root"
MYSQL_PASSWORD = "purelove"

SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"