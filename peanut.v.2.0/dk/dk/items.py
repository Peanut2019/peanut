# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    district = scrapy.Field()
    house = scrapy.Field()
    monthly = scrapy.Field()
    house_info = scrapy.Field()
    cfg = scrapy.Field()
    imgs = scrapy.Field()
    chum = scrapy.Field()
    traffic = scrapy.Field()
