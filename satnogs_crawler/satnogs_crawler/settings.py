# -*- coding: utf-8 -*-

# Scrapy settings for satnogs_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'satnogs_crawler'

SPIDER_MODULES = ['satnogs_crawler.spiders']
NEWSPIDER_MODULE = 'satnogs_crawler.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'satnogs_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_URI = 'data/%(time)s.json'
FEED_FORMAT = 'json'

ITEM_PIPELINES = {'satnogs_crawler.pipelines.SatnogsCrawlerPipeline': 1}
FILES_STORE = 'files'