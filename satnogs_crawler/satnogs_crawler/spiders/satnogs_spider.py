import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from satnogs_crawler.items import SatnogsCrawlerItem

def add_url_base(url):
    return "https://network.satnogs.org" + url

class SatnogsSpider(CrawlSpider):
    name = "satnogs"

    def __init__(self, noradId=None, *args, **kwargs):
        if (noradId == None):
            print('\nDefine a norad ID. Do it by using `scrapy crawl satnogs -a noradId=XXXXX` in console.')
        else:
            self.allowed_domains = ['network.satnogs.org']
            self.start_urls = [
                'https://network.satnogs.org/observations/?norad=' + noradId
            ]
            self.rules = (
                Rule(LinkExtractor(allow=(), restrict_css=('ul.pagination li:last-child')),
                     callback="parse_start_url",
                     follow=True),)
            super(SatnogsSpider, self).__init__(*args, **kwargs)

    def parse_start_url(self, response):
        item_links = response.css('.obs-link::attr(href)').extract()
        for link in item_links:
            yield scrapy.Request(add_url_base(link), callback=self.parse_observation_page)

    def parse_observation_page(self, response):
        observationId = response.css('#observation-info::text').extract()[0].strip()
        startDate = response.css('.datetime-data .datetime-date::text').extract()[0] + " " + response.css('.datetime-data .datetime-time::text').extract()[0]
        endDate = response.css('.datetime-data .datetime-date::text').extract()[1] + " " + response.css('.datetime-data .datetime-time::text').extract()[1]

        audioUrl = add_url_base(response.css('.front-line:last-child .front-data a::attr(href)').extract()[0])
        waterfallUrl = add_url_base(response.css('.front-line:last-child .front-data a::attr(href)').extract()[1])

        item = SatnogsCrawlerItem(id=observationId, startDate=startDate, endDate=endDate, url=response.url, file_urls=[audioUrl, waterfallUrl])
        yield item