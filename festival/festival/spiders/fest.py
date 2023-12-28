import scrapy
import json


class FestSpider(scrapy.Spider):
    name = "fest"
    allowed_domains = ["www.skiddle.com"]
    start_urls = ["https://www.skiddle.com/festivals/mainstream-pop.html"]

    def __init__(self, link='https://www.skiddle.com'):
        self.link = link

    def parse(self, response):
        host = 'https://www.skiddle.com/festivals/mainstream-pop.html'

        img = response.xpath('.//div[@class="card   flex-height lvl-1 brt-5px bg-white relative has-details"]/a/img/@src').getall()

        yield scrapy.Request(url=host, cb_kwargs={'img': img}, callback=self.parse_data)

    def parse_data(self, response, img):
        bloks = response.xpath('//div[@class="pad-10 card-info "]')
        for blok in bloks:
            name = blok.xpath('./h3/a/text()').getall()#get(default='')
            city = blok.xpath('./div[@class="p-9pt tc-grey margin-bottom-10"]/p[1]/span/text()').getall()#get(default='')
            data = blok.xpath('./div[@class="p-9pt tc-grey margin-bottom-10"]/p[2]/span/text()').getall()#get(default='')
            url = self.link + blok.xpath('./a/@href').get(default='')
            i = {'name': name,
                 'city': city,
                 'data': data,
                 'url': url,
                 'img_url': img}
            yield i
            # yield scrapy.Request(url=self.start_urls, cb_kwargs={'img': img, 'item': i}, callback=self.parse)

