import scrapy
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
from scrapy import FormRequest
import pandas as pd


class PriceSpider(scrapy.Spider):
    name = "price"
    start_urls = ["https://fcainfoweb.nic.in/reports/report_menu_web.aspx"]

    def parse(self, response):
        #open_in_browser(response)
        data = {'ctl00$MainContent$Ddl_Rpt_type': 'Retail',
                'ctl00$MainContent$ddl_Language': 'English',
                'ctl00$MainContent$Rbl_Rpt_type': 'Price report'}
        yield FormRequest.from_response(response, formdata=data, callback=self.step2)

    def step2(self, response):
        #open_in_browser(response)
        data = {'ctl00$MainContent$Ddl_Rpt_Option0': 'Daily Prices'}
        yield FormRequest.from_response(response, formdata=data, callback=self.step3)

    def step3(self, response):
        #open_in_browser(response)
        data = {'ctl00$MainContent$Txt_FrmDate': '06/03/2024',
                'ctl00$MainContent$btn_getdata1': 'Get Data'}
        yield FormRequest.from_response(response, formdata=data, callback=self.parse_table)

    def parse_table(self, response):
        dfs = pd.read_html(response.text)
        for i,df in enumerate(dfs):
            df.to_csv(f'data_{i}.csv')




