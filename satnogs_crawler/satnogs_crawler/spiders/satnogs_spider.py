import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SatnogsSpider(CrawlSpider):
    name = "satnogs"

    allowed_domains = ["network.satnogs.org"]
    start_urls = [
        'https://network.satnogs.org/observations/?norad=44427'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('ul.pagination li:last-child',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)