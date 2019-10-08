# -*- coding: utf-8 -*-

import scrapy

class SatnogsCrawlerItem(scrapy.Item):
    id = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    audioUrl = scrapy.Field()
    waterfallUrl = scrapy.Field()
    url = scrapy.Field()

    pass
