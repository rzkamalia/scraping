import scrapy

class SecondProjectSpider(scrapy.Spider):
    name = "second_project"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        containers = response.xpath('(//div[@class = "adbl-impression-container "]/div/span)[2]/ul/li')
        for container in containers:
            title = container.xpath('.//li/h3[contains(@class, "bc-heading")]/a/text()').getall()
            subtitle = container.xpath('.//li[contains(@class, "subtitle")]/span/text()').getall()
            author = container.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            narrator = container.xpath('.//li[contains(@class, "narratorLabel")]/span/a/text()').getall()
            language = container.xpath('.//li[contains(@class, "languageLabel")]/span/text()').getall()
            language = [language.strip().replace('\n', '').replace(' ', '').split(':')[1].strip() for language in language]

            yield {
                'title': title,
                'subtitle': subtitle,
                'author': author,
                'narrator': narrator,
                'language': language
            }
        
        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page_url = pagination.xpath('.//li/span[contains(@class, "nextButton")]/a/@href').get()
        if next_page_url:
            yield response.follow(url = next_page_url, callback = self.parse)