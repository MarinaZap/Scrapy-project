import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CimmytNewsSpider(CrawlSpider):
    name = "cimmyt_news"
    allowed_domains = ["www.cimmyt.org"]
    start_urls = ["https://www.cimmyt.org/category/multimedia/?category=news&theme=0&location=0&resea"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='sf-card__text']/h3/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='nav-links']/a/@href"))
    )

    def parse_item(self, response):
        item = {}
        item["name"] = response.xpath('//div[@class="sf-article-header__title-container"]/h1/text()').get()
        if item:
            item["title"] = response.xpath('//div[@class="sf-card__excerpt"]/p/text()').get()
        else:
            item["title"] = ''
        if item:
            item["author"] = response.xpath('//div[@class="sf-author"]/a/text()').get()
        else:
            item["author"] = ''
        if item:
            item["data"] = response.xpath("//div[@class='sf-card__text-meta']/time/text()").get()
        else:
            item["data"] = ''
        return item


        # item = {}
        # item["name"] = response.xpath('//div[@class="sf-article-header__title-container"]/h1/text()').get()
        # if item:
        #     item["title"] = response.xpath('//div[@class="sf-article-header"]/h3/text()').get()
        # else:
        #     item["title"] = ''
        # if item:
        #     item["author"] = response.xpath('//div[@class="sf-author"]/a/text()').get()
        # else:
        #     item["author"] = ''
        # if item:
        #     item["data"] = response.xpath("//div[@class=\"sf-author\"]/time/text()").get()
        # else:
        #     item["data"] = ''
        # return item
