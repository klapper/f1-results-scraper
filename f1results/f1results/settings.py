# -*- coding: utf-8 -*-

# Scrapy settings for f1results project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'f1results'

SPIDER_MODULES = ['f1results.spiders']
NEWSPIDER_MODULE = 'f1results.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'f1results (+http://www.yourdomain.com)'

#uncomment to use proxy
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'f1results.middlewares.ProxyMiddleware': 100,
#}