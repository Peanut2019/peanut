from lxml import etree
import requests
all_url = []

# 门头沟区 无数据信息
# 朝阳区 丰台区  请求无数据
# 朝阳区 丰台区 海淀区 石景山区 通州区 昌平区 大兴区 房山区
# 东城区 西城区 朝阳区 海淀区 丰台区 石景山区 通州区 昌平区 大兴区 顺义区 房山区 门头沟区
# p2500-d东城区.html
quyu = ['东城区', '西城区', '朝阳区', '海淀区', '丰台区', '石景山区', '通州区', '昌平区', '大兴区', '顺义区', '房山区', '门头沟区']
#所有城区的房屋总url

# 得到quyu_2ye中所有的房屋url
def hous_url():
    quyu_house = []
    for i in quyu:
        for c in range(1, 16):
            # print(c)
            url = 'https://www.danke.com/room/bj/p2500-d{}.html?page={}'.format(i, c)
            res = requests.get(url)
            house = etree.HTML(res.text, etree.HTMLParser())
            house_url = house.xpath("//div[@class='r_lbx_cena']/a/@href")
            # print('--------------------------------->{}'.format(c),house_url)
            if house_url != []:
                quyu_house.append(house_url)
            else:
                break
    return quyu_house
ex_house = hous_url() #最终房屋url

for hou_url in ex_house:
    all_url.append(hou_url)
print(len(all_url))