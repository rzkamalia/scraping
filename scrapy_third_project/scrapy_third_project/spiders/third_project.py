import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time

class ThirdProjectSpider(CrawlSpider):
    name = "third_project"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies_letter-Z"]

    # below code means: we will follow only the links of the elements that have this XPath
    rules = (
        Rule(LinkExtractor(restrict_xpaths = ('//ul[contains(@class, "scripts-list")]/a')), callback = "parse_item", follow = True),
        Rule(LinkExtractor(restrict_xpaths = ('(//a[@rel="next"])[1]'))),
    )

    def parse_item(self, response):
        article = response.xpath('//article[@class = "main-article"]')
        time.sleep(1) # if we dont add sleep, only first page that will scraped
        yield {
            'title': article.xpath('./h1/text()').get(),
            'plot': article.xpath('./p/text()').get(),
            # 'transcript': article.xpath('./div[@class = "full-script"]').getall(),
            'url': response.url
        }