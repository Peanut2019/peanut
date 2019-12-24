# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from dk.items import DkItem
import pymysql
class DkPipeline(object):
    def process_item(self, item, spider):
        return item
class DankePipeline(object):
    def get_media_requests(self, item, info):
        if isinstance(item, DkItem):
            yield Request(item['url'])

class MysqlPipeline(object):
    """
    同步操作
    """
    # item = DkItem()
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(host='localhost',user= 'root',passwd= '123456',db= 'pythonclass',port=3306,charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql语句
        insert_sql = """
        insert into bjdanke(district,house,monthly,house_info,cfg,imgs,chum,traffic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['district'], item['house'], item['monthly'], item['house_info'],
                                         item['cfg'],item['imgs'],item['chum'],item['traffic']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
