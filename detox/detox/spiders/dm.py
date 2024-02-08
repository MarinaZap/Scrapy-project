import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DmSpider(CrawlSpider):
    name = "dm"
    allowed_domains = ["www.thedetoxmarket.com"]
    # start_urls = ["https://www.thedetoxmarket.com/"]
    start_urls = ["https://www.thedetoxmarket.com/pages/brand-list"]

    # rules = (Rule(LinkExtractor(allow='/collections/makeup', restrict_xpaths='.//div[@class="column third brand-list--brand"]/a/@href'), callback='parse', follow=True))
    rules = (
        Rule(LinkExtractor(allow='/collections/makeup'), callback='parse', follow=True),
        Rule(LinkExtractor(allow='/collections/body'), callback='parse', follow=True)
    )
    # rules = (
    #     Rule(LinkExtractor(allow='/collections/face-makeup'), callback='parse', follow=True),
    # )

    # Rule(LinkExtractor(restrict_xpaths='//div[@class="column third brand-list--brand"]/a/@href'),
    #      callback='parse', follow=True)
    def parse(self, response):
        for blok in response.xpath('.//div[@class="product-block__inner"]'):
            name_firma = blok.xpath(
                './/div[@class="product-vendor-price-wrapper d-flex"]/div[@class="vendor"]/text()').get()
            # print(name_firma)
            name_product = blok.xpath('.//div[@class="product-block__title-price"]/a[@class="title"]/span/text()').get()
            # print(name_product)
            # if response.xpath('.//div[@class="price align-right "]') is not None:
            price = blok.xpath('.//div[@class="product-vendor-price-wrapper d-flex"]/div[2]/span[@class="amount theme-money"]/text()').get(default='').strip()

            yield {
                'Name_firma': name_firma,
                'Name_product': name_product,
                'Price': price
            }
