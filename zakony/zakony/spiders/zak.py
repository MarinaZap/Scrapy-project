import scrapy


class ZakSpider(scrapy.Spider):
    name = "zak"

    def start_requests(self):
        yield scrapy.Request(url='https://library.siam-legal.com',
                             callback=self.parse_data)

    def parse_data(self, response):
        for href in response.xpath('.//ul[@class="sub-menu"]/li/a/@href').getall():
            # print(href)
            yield response.follow(href, callback=self.parse_item)

    def parse_item(self, response):
        for link in response.xpath('//td[@data-title="Law Description"]/a/@href').getall():
            # print(link)
            yield response.follow(link, callback=self.parse_list)

    def parse_list(self, response):
        i = {}
        for blok in response.xpath('//div[@id="tabs"]'):
            name = blok.xpath('.//div[@class="title1 clearfix"]/h4/text()').get(default='')
            # print(name)
            text = blok.xpath('.//p/text()').get(default='')
            # print(text)

            next_page = response.xpath('.//span[@class="fr next-pagination"]/a/@href').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

            i['name'] = name
            i['text'] = text
            yield i
