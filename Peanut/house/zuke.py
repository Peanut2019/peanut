import requests
from lxml import etree
import time
url = 'https://bj.zuke.com'
url1 = 'https://bj.zuke.com/fang?district=&region=&line=&station=&bedroom=&rentstart=0&rentend=4000&characteristic=&decoration=&orientation=&search='
headers = {
'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1 '

}


res = requests.get(url1,headers=headers)

print(res.status_code)


# print(res.text)

quyu = etree.HTML(res.text, etree.HTMLParser())
qu_url = quyu.xpath("//div[@class='left']//a/@href")
quyu_url = []
house_url = []
def quyu(): #所有城区的url
    for i in qu_url[1:17]:
        print('-------------------------------------1',i)
        quyu_url.append(url+i)
    return quyu_url
hou = quyu()
# print(hou)
def hous_url():#所有房间url
    for i in hou:
        for a in range(1,10):
        # print(requests.status_codes)
        #     print(i)
            print('---------------------------------------------2',i)
            resq = requests.get(i+'&page={}'.format(a),headers=headers)
            # print(resq.text)
            hos = etree.HTML(resq.text,etree.HTMLParser())
            home_url = hos.xpath("//a[@class='list-item clearfix']/@href")
            # print(home_url)
            house_url.append(home_url)
    return house_url
home_details = hous_url()
new_home_url = []
for i in home_details:
    if i != []:
        print('--------------------------------------------3',i)
        new_home_url.append(i)
print(new_home_url)
def home_message():
    for i in new_home_url:
        for b in i:
#             print(url+b)
            resa = requests.get(url+b)
            home_mess = etree.HTML(resa.text,etree.HTMLParser())
            district = home_mess.xpath("//span[@class='c-333']/text()")[7]#房屋所在区
            district = ' '.join(district)
            print(district)
            house = home_mess.xpath("//span[@class='c-333 left']/text()")#房屋所在位置
            house = ' '.join(house)
            print(house)
            monthly = home_mess.xpath("//span[@class='f26 bold']/text()")#月租
            monthly = ' '.join(monthly)+'元/月'
            print(monthly)
            house_info = home_mess.xpath("//span[@class='c-333']/text()")#房屋信息
            house_info = ' '.join(house_info)
            print(house_info)
            agent = home_mess.xpath("//p[@class='mt4 f18 c-333']/text()")#房地产经纪人
            agent_phone = home_mess.xpath("//span[@class='f16 c-ff5555']/text()")
            agent = ' '.join(agent)+':'+' '.join(agent_phone)
            print(agent)
            imgs = home_mess.xpath("//img[@class='zooming-switch']/@src")#房屋图片展示
            imgs = ' '.join(imgs)
            print(imgs)
            traffic = home_mess.xpath("//div[@class='plr20 c-333 f14']/text()")#房屋所在地周围环境
            traffic = ' '.join(traffic)
            print(traffic)
            property_fee = ' '.join('无物业费!')
            print(property_fee)

home_message()

