import scrapy


class BooksCrawlSpider(scrapy.Spider):
    name = "books_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath("//ol[@class='row']/li")
        for book in books:
            yield {
                'image': book.xpath(".//div[@class='image_container']/a/img/@src").get(),
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath (".//p[@class='price_color']/text()").get()
            }
