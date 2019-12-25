# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
from scrapy import Request
# from zk.items import ZkItem
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class FangziPipeline(object):
    def process_item(self, item, spider):
        return item


# class LianjiaPipeline(object):
#     def __init__(self):
#         self.fp = open('lianjia.json', 'wb')
#         self.zufang_exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
#
#     def process_item(self, item, spider):
#         self.zufang_exporter.export_item(item=item)
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()


# 11111111111111111111111111111111111111111111
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.pipelines.images import ImagesPipeline


# import pymysql
# class DkPipeline(object):
#     def process_item(self, item, spider):
#         return item
# class DankePipeline(object):
#     def get_media_requests(self, item, info):
#         if isinstance(item, ZkItem):
#             yield Request(item['url'])


url = "mysql+pymysql://root:111111@127.0.0.1:3306/python1904?charset=utf8mb4"
engine = create_engine(url, echo=False, encoding="utf-8")
Base = declarative_base()
metadata = MetaData(engine)


# 这个暂时没啥用， 也可以按照这种的去改，但是这份儿代码没用到
# class User(Base):
#     __table__ = Table("bjdanke", metadata, autoload=True) # User是表名


class WlcbCloudPipeline(object):

    def open_spider(self, spider):
        self.SessionClass = sessionmaker(bind=engine)  # 利用工厂模式获取SessionClass
        self.session_obj = self.SessionClass()  # 创建session对象,此时已绑定数据库引擎，但是未关联任何的对象模型
        self.User_table = Table("bj5i5j", metadata, autoload=True)  # autoload=True这个是关键

    def process_item(self, item, spider):
        self.session_obj.execute(self.User_table.insert(), [item])  # item是{"id":1,"name":"xxx"}
        # self.User_table.insert(id=1, name="2")
        self.session_obj.commit()

        return item

    def close_spider(self, spider):
        self.session_obj.close()
        self.session_obj.commit()
