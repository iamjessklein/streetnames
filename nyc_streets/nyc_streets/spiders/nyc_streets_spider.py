import scrapy

from nyc_streets.items import NycStreet

class NycStreetSpider(scrapy.Spider):
    name = 'nyc'
    allowed_domains = ["nycstreets.info"]
    start_urls = [
        "http://nycstreets.info/honorStreet.asp?b=BX&letter=%23",
        "http://nycstreets.info/honorStreet.asp?b=BK&letter=%23",
        "http://nycstreets.info/honorStreet.asp?b=M&letter=%23",
        "http://nycstreets.info/honorStreet.asp?b=Q&letter=%23",
        "http://nycstreets.info/honorStreet.asp?b=SI&letter=%23"

    ]

    def parse(self, response):
        for href in response.css("#letterlist > a.letterlink::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_street_page)

    # def parse(self, response):
    #     for sel in response.xpath('//div[@class="streetentry"]'):
    #         name = sel.xpath('b/text()').extract()
    #         street = NycStreet()
    #         street['name'] = name[0]
    #         texts = sel.xpath('text()').extract()
    #         borough = texts[0].strip().replace('(', '').replace(')', '')
    #         street['borough'] = borough
    #         street['present_name'] = texts[1]
    #         street['location'] = texts[2]
    #         street['desc'] = texts[3]
    #         street['local_law'] = texts[4]
    #         yield street

    def parse_street_page(self, response):
        for sel in response.xpath('//div[@class="streetentry"]'):
            name = sel.xpath('b/text()').extract()
            street = NycStreet()
            street['name'] = name[0]
            texts = sel.xpath('text()').extract()
            borough = texts[0].strip().replace('(', '').replace(')', '')
            street['borough'] = borough
            street['present_name'] = texts[1]
            street['location'] = texts[2]
            street['desc'] = texts[3]
            yield street
