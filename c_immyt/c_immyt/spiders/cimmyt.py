import scrapy


class CimmytSpider(scrapy.Spider):
    name = "cimmyt"
    allowed_domains = ["www.cimmyt.org"]
    start_urls = ["https://www.cimmyt.org/category/multimedia/?category=news&theme=0&location=0&resea"]

    # def __init__(self, name, data, url, author):
    #     self.name = name,
    #     self.data = data,
    #     self.url = url,
    #     self.author = author

    def parse(self, response, **kwargs):
        cards = response.xpath('//div[@class="sf-card__text"]')
        for card in cards:
            name = card.xpath('.//h3/a/text()').get(default='')
            url = card.xpath('.//h3/a/@href').get(default='')
            date = card.xpath(f'.//time/text()').get(default='')
            yield scrapy.Request(url, callback=self.parse_page, meta={'URL': url, 'Name': name, 'Date': date})

        next_page_url = response.xpath('//div[@class="nav-links"]/a/@href').get(default='')
        if next_page_url:
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_page(self, response):
        url = response.meta.get('URL')
        name = response.meta.get('Name')
        date = response.meta.get('Date')

        for link in response.xpath('//div[@class="sf-card__text"]/h3/a/@href'):
            yield response.follow(link.get(), callback=self.parse)

        article = response.xpath('//div[@class="sf-article-header"]')
        if article:
            author = article.xpath("//div[@class=\"sf-author\"]/a/text()").get(default='')
        else:
            author = ''

        yield {'Url': url, 'Name': name, 'Date': date, 'Author': author}