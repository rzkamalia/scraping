import scrapy
import pandas as pd

class FirstProjectSpider(scrapy.Spider):
    name = "first_project"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        for country in response.xpath('//td/a'):
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            # absolute url
            # absolute_url = f'https://www.worldometers.info{country_link}'
            # other way:
            # absolute_url = response.urljoin(country_link)
            # yield scrapy.Request(url = absolute_url)

            # relative url
            yield response.follow(url = country_link, callback = self.parse_country, meta = {'country': country_name})

    def parse_country(self, response):
        country = response.request.meta['country']
        headers = response.xpath('(//table[contains(@class, "table")])[1]/thead/tr/th')
        
        cleaned_headers = []
        for header in headers:
            br_text = header.xpath('.//br/following-sibling::text()').get()
            if br_text:
                cleaned_headers.append(header.xpath('.//text()').get().strip() + ' ' + br_text.strip())
            else:
                cleaned_headers.append(header.xpath('.//text()').get().strip())

        yield {
            'country': country,
            'header': cleaned_headers,
        }
        
        rows = response.xpath('(//table[contains(@class, "table")])[1]/tbody/tr')
        for row in rows:
            columns = row.xpath('./td')
            row_data = {}

            for i in range(len(columns)):
                column_name = cleaned_headers[i]
                column_data = columns[i].xpath('.//text()').get()

                row_data[column_name] = column_data.strip() if column_data else None

            yield {
                'country': country,
                'row': row_data,
            }

        # rows = {}
        # for i in range(0, len(cleaned_headers)):
        #     row = response.xpath(f'(//table[contains(@class, "table")])[1]/tbody/tr/td[{i+1}]')
        #     row = [row.xpath('.//text()').get() for row in row]
            
        #     rows[cleaned_headers[i]] = row

        #     print('rows', rows)

        # df = pd.DataFrame.from_dict(rows)
        # df.to_csv(f'scrapy_population_{country}.csv', index = False)
        # print(f'process done, scrapy_population_{country}.csv created')