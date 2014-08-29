# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class F1ResultsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    team = scrapy.Field()
    position = scrapy.Field()
    grid = scrapy.Field()
    points = scrapy.Field()
    driver_name = scrapy.Field()
    pass
