import scrapy


class QoutEsSpider(scrapy.Spider):
    name = "qout_es"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quot in response.xpath("//div[@class='quote']"):
            yield {
                'text': quot.xpath("//span[@class='text']/text()").getall(),
                'author': quot.xpath("//small[@class='author']/text()").getall()
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
