import scrapy


class Book24Spider(scrapy.Spider):
    name = "book24"
    allowed_domains = ["book24.ua"]
    start_urls = ["https://book24.ua/ua/catalog/saleleader/"]

    def parse(self, response):
        for link in response.css('div.image_wrapper_block a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

        for i in range (1, 5):
            next_page = f'https://book24.ua/ua/catalog/saleleader/?PAGEN_1={i}'
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        yield{
            'name':response.css('div.topic__heading h1::text').get(),
            'price':response.css('span.price_value::text').get(),
            'realiry':response.css('div.quantity_block_wrapper span::text').get()
            }
