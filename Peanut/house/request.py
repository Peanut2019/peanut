#!/usr/bin/python
# coding:utf-8
# time:2019-12-19 14:03:05

from lxml import etree
import re
import requests


def change():
    pass
    # 解析出来的一个的url
    url0 = 'https://bj.5i5j.com/zufang/90185908.html'
    res = requests.get(url0)
    pattern = r"href='(.+?)';"  # 匹配规则
    regex = re.compile(pattern)  # 语法
    res_text = res.text  # 获取网页的全部源码.
    res_list = regex.findall(res_text)  # 匹配出.list
    print(res_list[0])


# change()


with open('house_xq.html', encoding='utf8')as f:
    res = f.read()
# print(res)
html = etree.HTML(res, etree.HTMLParser())

# 以下的解析都是list格式,记得索引出来

# 地区 todo
# 房子位置
# title = html.xpath('//h1[@class="house-tit"]/text()')

# 月租
# jine = html.xpath('//p[@class="de-price"]/span/text()')

# 房子信息
# xiaoqu = html.xpath('//div[@class="zushous"]//text()')
# xiangqing = html.xpath('//div[@class="house-infor clear"]//p/text()')

# 经纪人
# zhongjie_name = html.xpath('//li[@class="daikcon fl"]/h3/a/text()')
# zhongjie_jieshao = html.xpath('//li[@class="daikcon fl"]/p/text()')
# zhongjie_tel = html.xpath('//li[@class="daikcon fl"]/label/text()')
# zhongjie_img = html.xpath('//div[@class="daikansty "]/ul/li[1]/a/img')
# zhongjie_img[0].get('src')

# 房子img
# house_img = html.xpath('//div[@class="infocontent"]/ul//li/a')
# for i in house_img:
#     print(i.get('href'))

# 交通
# zhongjie_img = html.xpath('//div[@class="zhishu_content"]//p/text()')

# 物业费 --暂无

with open('house_index.html', encoding='utf8')as f2:
    res2 = f2.read()
# print(res)
html2 = etree.HTML(res2, etree.HTMLParser())
title = html2.xpath('//h1[@class="house-tit"]/text()')
