import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from satnogs_crawler.items import SatnogsCrawlerItem

def add_url_base(url):
    return "https://network.satnogs.org" + url

class SatnogsSpider(CrawlSpider):
    name = "satnogs"

    allowed_domains = ["network.satnogs.org"]
    start_urls = [
        'https://network.satnogs.org/observations/?norad=44427'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('ul.pagination li:last-child',)),
             callback="parse_start_url",
             follow=True),)

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

        item = SatnogsCrawlerItem(id=observationId, startDate=startDate, endDate=endDate, audioUrl=audioUrl, waterfallUrl=waterfallUrl, url=response.url)
        yield item