import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from satnogs_crawler.items import SatnogsCrawlerItem


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
            yield scrapy.Request("https://network.satnogs.org" + link, callback=self.parse_observation_page)

    def parse_observation_page(self, response):
        observationId = response.css('#observation-info::text').extract()[0].strip()
        startDate = response.css('.datetime-data .datetime-date::text').extract()[0] + " " + response.css('.datetime-data .datetime-time::text').extract()[0]
        endDate = response.css('.datetime-data .datetime-date::text').extract()[1] + " " + response.css('.datetime-data .datetime-time::text').extract()[1]

        item = SatnogsCrawlerItem()
        item['id'] = observationId
        item['startDate'] = startDate
        item['endDate'] = endDate
        item['url'] = response.url
        yield item