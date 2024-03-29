#!/usr/bin/python
# coding:utf-8
# time:2019-12-19 14:13:31

# -*- coding: utf-8 -*-
import scrapy
import re
from fangzi.items import FangziItem

DATA = []


class HouseSpider(scrapy.Spider):
    name = 'lian_jia'  # 爬虫的唯一id
    # 名字这个字段还没有设置好.
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang/erp3000/']  # 起始的list,或者下面的函数,效果是一样的

    def parse(self, response, **kwargs):
        item = FangziItem()
        areas = response.xpath('//ul[@data-target="area"]//li/a/text()').getall()  # 朝阳,延庆...

        area_url_list = response.xpath('//ul[@data-target="area"]//li/a/@href').getall()
        area_urls = list(map(lambda url: response.urljoin(url), area_url_list))  # 智能拼str,加上http前缀,哪里没有补哪里
        # print('area的url------>',area_urls)
        for i in range(1, len(area_urls)):
            if areas[i] == '亦庄开发区':
                item['area'] = areas[i]
                url = area_urls[i]
            else:
                item['area'] = areas[i] + '区'
                url = area_urls[i]

            # print(areas[area_urls.index(i)])
            yield scrapy.Request(url=url, callback=self.detail_parse, meta={'item': item['area']})
            # break

    def detail_parse(self, response):
        houseList = response.xpath('//div[@class="content__list"]/div/a/@href').getall()
        # 单个界面的所有房间的url
        houseList_urls = list(map(lambda url: response.urljoin(url), houseList))
        # print('----' * 30, houseList_urls)
        # pages = response.xpath('//div[@class="fanye"]/a/@href').getall()
        # pages_url = list(map(lambda url: response.urljoin(url), pages))
        areas = response.meta['item']
        print(areas, '##########')
        for page_url in houseList_urls:
            yield scrapy.Request(url=page_url, callback=self.info_parse, meta={'item': areas})
            # break

    def info_parse(self, response):
        item = FangziItem()
        title = response.xpath('//div[@class="content clear w1150"]/p/text()').get()
        title = re.sub(r'\s', '', title)  # 标题
        price = response.xpath('//div[@class="content__core"]/div[2]/div/span/text()').get()  # 价格
        house_info = response.xpath('//ul[@class="content__aside__list"]//li/text()').getall()  # 房屋info

        house_msgs1 = response.xpath('//div[@id="info"]/ul//li/text()').getall()
        house_msgss = [house_msg.strip() for house_msg in house_msgs1]
        house_msgss = ' '.join(house_msgss)  # '房屋信息内容,,'

        zhongjie_name = response.xpath('//span[@class="contact_name"]/text()').getall()
        tel = []
        zhongjie_tel = response.xpath('//p[@id="phone1"]/text()').get()
        tel.append(zhongjie_tel)
        # zhongjie = dict(zip(zhongjie_name, tel))  # 中介
        print('bug',zhongjie_name)
        print('bug',zhongjie_tel)
        if zhongjie_tel:
            zhongjie = ' '.join(zhongjie_name) + ':' + ''.join(zhongjie_tel)  # 中介
        else:
            zhongjie = zhongjie_name
        housePhotos = response.xpath('//ul[@id="prefix"]//li/img/@src').getall()  # 图片
        housePhotos = ' '.join(housePhotos)
        areas = response.meta['item']
        # print(44444444444444444444,areas)
        item['district'] = areas
        item['house'] = title
        item['monthly'] = price
        item['house_info'] = house_msgss
        item['agent'] = zhongjie
        item['imgs'] = housePhotos
        # item = FangziItem(district=areas, house=title, monthly=price, house_info=house_msgss,
        #                   agent=zhongjie, imgs=housePhotos)
        # print('这是我手打的标志位',title, price, house_info,house_msgss,zhongjie,housePhotos)
        # print('=' * 80)
        yield item
