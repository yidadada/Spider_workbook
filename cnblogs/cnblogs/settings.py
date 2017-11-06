# -*- coding: utf-8 -*-
import os
import pymongo

# Scrapy settings for cnblogs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnblogs'

SPIDER_MODULES = ['cnblogs.spiders']
NEWSPIDER_MODULE = 'cnblogs.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnblogs (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8
CONCURRENT_ITEMS = 8

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cnblogs.middlewares.CnblogsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'cnblogs.mymiddlewares.RandomUserAgent': 543,
    #'cnblogs.mymiddlewares.RandomIP': 544,
    'cnblogs.mymiddlewares.RandomKuaiDai': 1,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'cnblogs.pipelines.CnblogsPipeline': 300,
    # 'cnblogs.pipelines.cnblogs': 1,
    # 'cnblogs.pipelines.MySQLdbpilines': 2,
    #'cnblogs.pipelines.Tencentpilines': 5,
    #'cnblogs.pipelines.TencentMySQLdbpilines': 6,
   # 'cnblogs.pipelines.Xicipilines': 3,
   # 'cnblogs.pipelines.rootPipeline': 4,
}

#IMAGES_URLS_FIELD = 'image_url' # 指定从哪个字段提取图片链接
#base_dir = os.path.dirname(os.path.dirname(__file__))
#IMAGES_STORE = os.path.join(base_dir,'images') # 设置图片存放位置

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 请求超时
# DOWNLOAD_TIMEOUT = 5
# # 重新请求
# RETRY_ENABLED = True
# # 重试次数
# RETRY_TIMES = 3

USER_AGENS = [
    'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; LG; GW910)',
    'Mozproxyilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]

PROXY_IP = [
    {'host':'116.62.128.50:16816'},
    {'host': '183.49.85.71:8118'},
    {'host': '111.200.58.94:80'},
    {'host': '203.171.226.151:80'},
    {'host': '121.232.146.18:9000'},
    {'host': '121.232.144.182:9000'},
    {'host': '121.232.144.182:9000','auth':'1752570559:wd0p04kd'},

]

MONGO_HOST = "101.132.157.111"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGODB_DBNAME = 'd1' #数据库名
#MONGODB_DOCNAME = 'form' #表名


def getproxy():
    mongo_client = pymongo.MongoClient("101.132.157.111" ,27017)
    db = mongo_client[MONGODB_DBNAME]
    ip_list = db.text.find() #查找出的类型是对象
    PROXIES = []
    for ipp in ip_list:
        #ipp是dict
        PROXIES.append(ipp)
        return PROXIES

#PROXIES = getproxy()

