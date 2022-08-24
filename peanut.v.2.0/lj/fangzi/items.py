# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangziItem(scrapy.Item):
    area = scrapy.Field()
    district = scrapy.Field()  # 区
    house = scrapy.Field()  # 标题
    monthly = scrapy.Field()  # 价格
    house_info = scrapy.Field()  # 房简介
    # house_msgss = scrapy.Field()    # 房屋信息
    agent = scrapy.Field()  # 中介
    imgs = scrapy.Field()  # 房屋imgs
