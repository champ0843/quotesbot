# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

cric_url = "https://www.cricbuzz.com/profiles/25/sachin-tendulkar"
cric_url = "https://www.cricbuzz.com/profiles/1413/virat-kohli"
cric_url = "https://www.cricbuzz.com/profiles/1447/ajinkya-rahane"
cric_url = "https://www.cricbuzz.com/profiles/8733/lokesh-rahul"
#cric_url = "http://quotes.toscrape.com/"
#//*[@id="playerProfile"]/div[2]/div[2]/div/div[2]/table
def create_table(xpath,response):
    column = []
    data = []
    for quote in response.selector.xpath(xpath):
        for thead in quote.css("thead"):
            for trow in thead.css("tr"):
                column = trow.css("th::attr(title)").extract()
                column = ['Format'] + column
        for tbody in quote.css("tbody"):
            for trow in tbody.css("tr"):
                print(trow)
                print(trow.css("td > strong::text").extract())
                mid_dat = trow.css("td > strong::text").extract() + trow.css("td::text").extract()
                print(mid_dat)
                data.append(mid_dat)
    return pd.DataFrame(data = data,columns = column)

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        cric_url,
    ]

    record = pd.DataFrame()

    def parse(self, response):
        column = []
        data = []
        bat_record = create_table('//*[@id="playerProfile"]/div[2]/div[2]/div/div[2]/table',response)
        bowl_record = create_table('//*[@id="playerProfile"]/div[2]/div[2]/div/div[3]/table',response)
        print(data)
        print(column)
        print(bat_record)
        print(bowl_record)
        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))

