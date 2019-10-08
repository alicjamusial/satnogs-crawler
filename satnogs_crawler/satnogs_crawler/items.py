# -*- coding: utf-8 -*-

import scrapy

class SatnogsCrawlerItem(scrapy.Item):
    id = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    url = scrapy.Field()
    files = scrapy.Field()
    file_urls = scrapy.Field()

    pass
