# -*- coding: utf-8 -*-

# Scrapy settings for fangzi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fangzi'

SPIDER_MODULES = ['fangzi.spiders']
NEWSPIDER_MODULE = 'fangzi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'fangzi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3  # 下载延迟
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    # 'cookie': 'global_cookie=n4ttflmc6sf7k33e90bealwkz10k4jh8rmp; __utma=147393320.1534939058.1577168233.1577168233.1577168233.1; __utmc=147393320; __utmz=147393320.1577168233.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; city=www; Integrateactivity=notincludemc; integratecover=1; ASP.NET_SessionId=oblflnm3hsadqooqmqr5itty; Rent_StatLog=a81ac2a8-d133-439d-b361-86cfcb56f0e9; g_sourcepage=zf_fy%5Elb_pc; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; keyWord_recenthousebj=%5b%7b%22name%22%3a%22%e4%ba%94%e6%a3%b5%e6%9d%be%22%2c%22detailName%22%3a%22%e6%b5%b7%e6%b7%80%22%2c%22url%22%3a%22%2fhouse-a00-b02663%2f%22%2c%22sort%22%3a2%7d%2c%7b%22name%22%3a%22%e6%9c%9d%e9%98%b3%22%2c%22detailName%22%3a%22%22%2c%22url%22%3a%22%2fhouse-a01%2f%22%2c%22sort%22%3a1%7d%2c%7b%22name%22%3a%22%e9%80%9a%e5%b7%9e%22%2c%22detailName%22%3a%22%22%2c%22url%22%3a%22%2fhouse-a010%2f%22%2c%22sort%22%3a1%7d%5d; Captcha=6D334262307A6636447569363943725879364E3361774A647243724755762F6A6464554B6A4736614C346371556C4B384F656F4C643757622B614267425A332F4E432F76774546777557733D; __utmb=147393320.156.10.1577168233; unique_cookie=U_n4ttflmc6sf7k33e90bealwkz10k4jh8rmp*56'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'fangzi.middlewares.FangziSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'fangzi.middlewares.FangziDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'fangzi.pipelines.FangziPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
