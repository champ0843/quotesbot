# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

pela_url = "https://pelacase.com/pages/pela-case-yotpo-customer-reviews"
#cric_url = "http://quotes.toscrape.com/"
#//*[@id="playerProfile"]/div[2]/div[2]/div/div[2]/table
def create_table(xpath,response):
    column = []
    data = []
    print("getting insdie table")
    for quote in response.selector.xpath(xpath):
        print(quote)
        print(quote.extract())
        for thead in quote.css("div"):
            print(thead.extract())
            print(thead)
    #return pd.DataFrame(data = data,columns = column)

class ToScrapeCSSSpider(scrapy.Spider):
    name = "pela-spider"
    start_urls = [
        pela_url,
    ]

    record = pd.DataFrame()
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        column = []
        data = []
        bat_record = create_table('//*[@id="yotpo-testimonials-custom-tab"]/div',response)
        #bowl_record = create_table('//*[@id="playerProfile"]/div[2]/div[2]/div/div[3]/table',response)
        #print(data)
        #print(column)
        #print(bat_record)
        #print(bowl_record)
        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))

