from lxml import etree
import re
import requests
import time
#东城区 西城区 朝阳区 海淀区 丰台区 石景山区 通州区 昌平区 大兴区 顺义区 房山区 门头沟区
# p2500-d东城区.html
quyu = ['东城区', '西城区',' 朝阳区', '海淀区',' 丰台区', '石景山区', '通州区', '昌平区', '大兴区', '顺义区', '房山区', '门头沟区']
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
for i in quyu:
    print('----------------------->>>',i)
    url = 'https://www.danke.com/room/bj/p2500-d{}.html'.format(i)
    res = requests.get(url)
    # print(res.text)
    html = etree.HTML(res.text, etree.HTMLParser())
    time.sleep(5)
    # href = html.xpath("//div[@class='r_lbx_cena']/a/@href")
    name = html.xpath("//div[@class='r_lbx_cena']/a/@title")
    print(name)