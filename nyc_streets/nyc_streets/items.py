# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NycStreet(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    present_name = scrapy.Field()
    location = scrapy.Field()
    honoree = scrapy.Field()
    borough = scrapy.Field()
    desc = scrapy.Field()
    local_law = scrapy.Field()
