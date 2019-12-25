# -*- coding: utf-8 -*-
import scrapy
from zk.items import ZkItem

class ZukeSpider(scrapy.Spider):
    name = 'zuke'
    allowed_domains = ['bj.zuke.com']
    start_urls = ['https://bj.zuke.com/fang?district=&region=&line=&station=&bedroom=&rentstart=0&rentend=4000&characteristic=&decoration=&orientation=&search=']

    def parse(self, response):
        quyu_url = response.xpath("//div[@class='left']//a/@href")[1:17].getall()
        for i in quyu_url:
            for b in range(20):
                yield scrapy.Request('https://bj.zuke.com'+i+'&page={}'.format(b),callback=self.two_parse)
    def two_parse(self,response):
        hou = []
        print('-----------------------------------------------------------1')
        # print(response.url)
        house_url = response.xpath("//a[@class='list-item clearfix']/@href").getall()
        hou.append(house_url)
        # print(house_url)
        # print(hou)
        for i in hou[0]:
            print('--------------------------------------------------------2')
            # print('https://bj.zuke.com'+i)
            yield scrapy.Request('https://bj.zuke.com'+i,callback=self.three_parse)
    def three_parse(self,response):
        item = ZkItem()
        item['url'] = response.url
        print('--------------------------------------------------3')
        print(response.url)
        district = response.xpath("//span[@class='c-333 left']/text()").getall()[0][2:4]
        # print(district)
        district = ''.join(district)+'区'
        print(district)
        item['district'] = district
        house = response.xpath("//span[@class='c-333 left']/text()").getall()
        # print(house)
        house = ' '.join(house)
        print(house)
        item['house'] = house
        monthly = response.xpath("//span[@class='f26 bold']/text()").getall()
        monthly = ' '.join(monthly)
        print(monthly)
        item['monthly'] = monthly
        house_info = response.xpath("//span[@class='c-333']/text()").getall()
        house_info = ' '.join(house_info)
        print(house_info)
        item['house_info'] = house_info
        agent = response.xpath("//p[@class='mt4 f18 c-333']/text()").getall()
        agent_phone = response.xpath("//span[@class='f16 c-ff5555']/text()").getall()
        agent = ' '.join(agent) + ':' + ' '.join(agent_phone)
        print(agent)
        item['agent'] = agent
        imgs = response.xpath("//img[@class='zooming-switch']/@src").getall()
        imgs = ' '.join(imgs)
        print(imgs)
        item['imgs'] = imgs
        traffic = response.xpath("//div[@class='plr20 c-333 f14']/text()").getall()
        traffic = ' '.join(traffic)
        print(traffic)
        item['traffic'] = traffic
        property_fee = ' '.join('无物业费!')
        print(property_fee)
        item['property_fee'] = property_fee
        yield item