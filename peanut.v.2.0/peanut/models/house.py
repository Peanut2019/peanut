import datetime

from sqlalchemy import or_
from peanut.core.ext import db
from enum import Enum


class SourceEnum(Enum):
    LJ = "lj"
    ZK = 'zk'
    KNOWN = 'known'


class BaseModel(db.Model):
    __tablename__ = 'base_table'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DATETIME, default=datetime.datetime.now())


class District(BaseModel):
    __tablename__ = 'district_table'
    city = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)


class House(BaseModel):
    __tablename__ = 'house_table'
    source = db.Column(db.Enum, default=SourceEnum.KNOWN.value)
    district = db.Column(db.String(1000), nullable=False)  # 区
    house = db.Column(db.String(1000), nullable=False)  # 房子位置
    monthly = db.Column(db.Integer, nullable=False)  # 月租 int
    house_info = db.Column(db.String(1000), nullable=False)  # 房子信息
    agent = db.Column(db.String(1000), nullable=False)  # 房产经纪人
    images = db.Column(db.ARRAY(), nullable=False)  # 房间图片
    traffic = db.Column(db.String(1000), nullable=False)  # 交通
    property_fee = db.Column(db.String(1000), nullable=False)  # 物业费


#
# 添加数据
def add_house(district, house, monthly, house_info, agent, imgs):
    res = House(district, house, monthly, house_info, agent, imgs)
    db.session.add(res)
    db.session.commit()
    return True


# 显示全部
def query_all():
    res = House.query.all
    return tuple(res())


# 查询图片
def query_img():
    tuple1 = ()
    res = House.query.all
    for i in res():
        tuple1 += (i.imgs,)
    # print(tuple1)
    return tuple1


# 查询位置
def query_house():
    tuple1 = ()
    res = House.query.all
    for i in res():
        tuple1 += (i.house,)
    return tuple1


# query_house()
def query_houseid():
    tuple1 = ()
    res = House.query.all
    for i in res():
        tuple1 += (i.id,)
    return tuple1


# 房子信息
def query_houseinfo():
    tuple1 = ()
    res = House.query.all
    for i in res():
        tuple1 += (i.house_info,)
    return tuple1


# 查月租
def query_housemonthly():
    tuple1 = ()
    res = House.query.all
    for i in res():
        tuple1 += (i.monthly,)
    return tuple1


# 根据 网站 查询
def query_by_web(web):
    res = House.query.filter_by(web=web).all()
    if res != []:
        return tuple(res)


# 根据 区 查询
def query_by_district(district):
    res = House.query.filter_by(district=district).all()
    if res != []:
        return tuple(res)


# 根据 id 查询
def query_by_id(id):
    res = House.query.filter_by(id=id).all()
    if res != []:
        return tuple(res)


# 模糊查询 小区名
def query_by_likehouse(house):
    res = House.query.filter(House.house.like("%" + house + "%") if house is not None else "").all()
    return tuple(res)


# 模糊查询 地铁名
def query_by_liketraffic(traffic):
    res = House.query.filter(House.traffic.like("%" + traffic + "%") if traffic is not None else "").all()
    if res != []:
        return tuple(res)


def query_likeall(input):
    res = House.query.filter(or_(
        House.district.like("%" + input + "%") if input is not None else "",
        House.house.like("%" + input + "%") if input is not None else "",
        House.monthly.like("%" + input + "%") if input is not None else "",
        House.house_info.like("%" + input + "%") if input is not None else "",
        House.traffic.like("%" + input + "%") if input is not None else "")).all()
    # print(res)
    if res != []:
        return tuple(res)


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
