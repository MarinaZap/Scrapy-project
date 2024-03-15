import scrapy


class SanSpider(scrapy.Spider):
    name = "san"
    allowed_domains = ["sandhill.io"]
    start_urls = ["https://sandhill.io/feeds?page=1"]
    headers = {
        'Cookie': '_care_around_me_session=OVQ4cUFVSmJiNWVDK2dDRWxmcHY4SUNiekUrYnArL0sxTWI1azMvaGtFMFUvdXN3Lyt0SXRDTzY1TzAzZTRsRDh3VnVZZVFWRkl1NTBqM005UnJ4QkdGblRvZW56TlJoVWw0dlpjTSs1NThUZGptdTBGTlJxMGk1UjFMZkdrbDl6UTk1QlRKZXkvY1MzYitmUTFLVEZnPT0tLUN3N2x6d05qdFAwcldkTmQycG9YZ1E9PQ%3D%3D--2e27c46110259c26d857c5a214d285ee6e0e8cee'
    }

    def start_requests(self):
        page_number = 1
        for page_number in range(1, 29):
            yield scrapy.Request(url=f"https://sandhill.io/feeds?page={page_number}", headers=self.headers, callback=self.parse_blok)

    def parse_blok(self, response):
        bloks = response.xpath('.//div[@class="col-xs-6 col-sm-6 col-md-4"]')
        for blok in bloks:
            name = blok.xpath('.//div[@class="card-body py-3 news"]/h5/a/text()').get()
            #print(name)
            link_dod = blok.xpath('.//div[@class="card-body py-3 news"]/h5/a/@href').get()
            #print(link_dod)
            link = 'https://sandhill.io' + link_dod
            #print(link)
            yield response.follow(link, cb_kwargs={'link': link, 'name': name}, callback=self.parse_data)



    def parse_data(self, response, link, name):

        title = response.xpath('//div[@class="d-flex"]//p/a/text()').getall()
        date_pub = response.xpath('//div[@class="d-flex"]//p[2]/text()').getall()
       # print(data_pub)
        yield {
            'Name': name,
            'Link': link,
            'Title': title,
            'Date_pub': date_pub
        }




