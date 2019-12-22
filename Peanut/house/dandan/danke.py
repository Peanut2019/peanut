from house_urls import *
import os
print('loding......')
def house_xinxi():
    for a in all_url:
        for b in a:
            print(b)
                # 请求所有房屋页面为两页的区
            hou_2 = requests.get(b)
            hou_2_message = etree.HTML(hou_2.text, etree.HTMLParser())
            district = hou_2_message.xpath("//div[@class='detail-roombox']/a/text()")
            district = ''.join(district)
            # print(district)   #区
            house = hou_2_message.xpath("//h1/text()")
            house = ''.join(house)
            # print(house) #房子位置
            monthly = hou_2_message.xpath("/html/body/div[3]/div[1]/div[2]/div[2]/div[3]/div[2]/div/span/div/text()")
            monthly = ''.join(monthly)
            # print(monthly) #月租
            house_info = hou_2_message.xpath("//div[@class='room-list']/label/text()")
                # 房子信息
            housa = []
            for hous in house_info:
                hous = hous.strip()
                if hous != '':
                    housa.append(hous)
                    house_info = ''.join(housa)
            # print(house_info)
                    # print(type(house_info))
            cfg = hou_2_message.xpath("//tr[2]/td/text()")[:5]
            cfg = ' '.join(cfg)
            # print(cfg)
            # 房间配置
            imgs = hou_2_message.xpath("//img[@class='img-responsive']/@src")
            for img in imgs:
                imgs = ''.join(img)
                # print(imgs)
            # 房间图片
            chum = hou_2_message.xpath("//div[@class='room_center']/table/tbody/tr//td//text()")
            chua = []
            for chu in chum:
                chu = chu.strip()
                if chu != '':
                    # print(chu.strip())
                    chua.append(chu)
            # print(''.join(chua))
            chum = ''.join(chua)
            # print(chum)
            # 室友
            traffic = hou_2_message.xpath("//div[@class='room-list']/label/text()")[-1:]
            # 交通
            traffic = ''.join(traffic)
            # print(traffic)
            with open('abc.txt','a',encoding='utf-8') as f:
                f.write(district)
                f.write('\n')
                f.write(house)
                f.write('\n')
                f.write(monthly)
                f.write('\n')
                f.write(house_info)
                f.write('\n')
                f.write(cfg)
                f.write('\n')
                f.write(chum)
                f.write('\n')
                f.write(traffic)
                f.write('\n')
                f.write('\n')
if __name__ == '__main__':
    house_xinxi()