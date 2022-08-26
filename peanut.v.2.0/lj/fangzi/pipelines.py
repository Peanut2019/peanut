# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from zk.items import ZkItem
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class FangziPipeline(object):
    def process_item(self, item, spider):
        return item


url = "mysql+pymysql://debian-sys-maint:Bd0RfgLzkLtvlkCB@82.157.238.91:3306/peanut?charset=utf8mb4"

engine = create_engine(url, echo=False, encoding="utf-8")
Base = declarative_base()
metadata = MetaData(engine)


# 这个暂时没啥用， 也可以按照这种的去改，但是这份儿代码没用到
# class User(Base):
#     __table__ = Table("bjdanke", metadata, autoload=True) # User是表名


class WlcbCloudPipeline(object):

    def __init__(self):
        super().__init__()
        self.session = None
        self.call_session = None
        self.use_table = None

    def open_spider(self, spider):
        self.session = sessionmaker(bind=engine)  # 利用工厂模式获取SessionClass
        self.call_session = self.session()  # 创建session对象,此时已绑定数据库引擎，但是未关联任何的对象模型
        self.use_table = Table("lj", metadata, autoload=True)  # 把table_name换成你的表名,autoload=True这个是关键

    def process_item(self, item, spider):
        self.call_session.execute(self.use_table.insert(), [item])  # item是{"id":1,"name":"xxx"}
        # self.User_table.insert(id=1, name="2")
        self.call_session.commit()

        return item

    def close_spider(self, spider):
        self.call_session.close()
        self.call_session.commit()
