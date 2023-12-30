import scrapy


class InlaSpider(scrapy.Spider):
    name = "inla"
    allowed_domains = ["inla1.org"]
    start_urls = ["https://inla1.org/page/%d/?s&category&location&a=true" % i for i in range(1, 72)]


    def parse(self, response):
        for link in response.xpath('.//div[@class="item-data"]//div[@class="item-title"]/a/@href'):
            yield response.follow(link, callback=self.parse_data)


    def parse_data(self, response):

        name = response.xpath('//div[@class="entry-title "]/div[@class="entry-title-wrap"]/h1/text()').get()
        bd1 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[2]/text()').get()
        bd2 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[3]/text()').get()
        bd3 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[4]/text()').get()
        bd4 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[5]/text()').get()
        bd5 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[6]/text()').get()
        bd6 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[7]/text()').get()
        bd7 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[8]/text()').get()
        bd8 = response.xpath('//div[@class="entry-title "]//nav[@class="breadcrumbs"]//a[9]/text()').get()
        adress = response.xpath('//div[@class="content"]//div[@class="address-data"]/p/text()').get()
        gps = response.xpath('//div[@class="content"]//div[@class="address-row row-gps"]//p/text()').get().strip()
        tel = response.xpath('//div[@class="content"]//div[@class="address-row row-telephone"]//span[@itemprop="telephone"]/a/text()').get()
        mail = response.xpath('//div[@class="content"]//div[@class="address-row row-email hide-email"]//div[@class="address-data"]/p/text()').get()
        web = response.xpath('//div[@class="content"]//div[@class ="address-row row-web"]//div[@class="address-data"]/p/a/text()').get()

        data = {
            'name': name,
            'bd1': bd1,
            'bd2': bd2,
            'bd3': bd3,
            'bd4': bd4,
            'bd5': bd5,
            'bd6': bd6,
            'bd7': bd7,
            'bd8': bd8,
            'adress': adress,
            'gps': gps,
            'tel': tel,
            'mail': mail,
            'web': web
        }

        yield data

