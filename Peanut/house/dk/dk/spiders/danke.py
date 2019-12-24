# -*- coding: utf-8 -*-
import scrapy
from dk.items import DkItem

class DankeSpider(scrapy.Spider):
    name = 'danke'
    allowed_domains = ['www.danke.com']
    start_urls = ['https://www.danke.com/room/bj/p2500.html']

    def parse(self, response):
        url = response.xpath("//div[@class='area-ls-wp']/a/@href").getall()
        url = url[:12]
        # print(len(url))#所有区的url
        for i in url:
            for b in range(1,10):
                # print(b)
                hos_url = i+'?page={}'.format(b)
                # print(hos_url)
                yield scrapy.Request(url=hos_url,callback=self.other_paser)
    def other_paser(self,response):
        # item = DkItem()
        hou = []
        # print(response.url)
        # print('---------------------------->ok')
        house_url =response.xpath("//div[@class='r_lbx_cena']/a/@href").getall()
        house_name =response.xpath("//div[@class='r_lbx_cena']/a/text()").getall()
        # print(house_url)
        hou.append(house_url)

        for i in hou[0]:
            # print(i)
            yield scrapy.Request(url=i,callback=self.parse2)
    def parse2(self,response):
        item = DkItem()
        item['url'] = response.url
        # pass
        print('-----------------------------------------')
        print(response.url)
        district = response.xpath("//div[@class='detail-roombox']//a/text()")[0].getall()
        print(district)
        district = ''.join(district)
        print(district)
        item['district'] = district
        house = response.xpath("//h1/text()").getall()
        house = ' '.join(house)
        print(house)
        item['house'] = house
        monthly = response.xpath("//div[@class='room-price-sale']/text()").getall()
        # print(monthly)
        monthly = ''.join(monthly)
        print(monthly)
        item['monthly'] = int(monthly)
        house_info = response.xpath("//div[@class='room-list']/label/text()").getall()
        hou = []
        for house in house_info:
            house = house.strip()
            if house != '':
                hou.append(house)
                house_info = ''.join(hou)
        print(house_info)
        item['house_info'] = house_info
        cfg =  response.xpath("//tr[2]/td/text()")[:5].getall()
        cfg = ' '.join(cfg)
        print(cfg)
        item['cfg'] = cfg
        imgs = response.xpath("//img[@class='img-responsive']/@src")[:6].getall()

        imgs = ' '.join(imgs)
        print(imgs)
        # print(type(imgs))
        item['imgs'] = imgs
        chum = response.xpath("//div[@class='room_center']/table/tbody/tr//td//text()").getall()
        chua = []
        for chu in chum:
            chu = chu.strip()
            if chu != '':
                # print(chu.strip())
                chua.append(chu)

                chum = ' '.join(chua)
                item['chum'] = chum
        print(chum)

        traffic = response.xpath("//div[@class='room-list']/label/text()")[-1:].getall()
        traffic = ' '.join(traffic)
        print(traffic)
        item['traffic'] = traffic
        yield item
