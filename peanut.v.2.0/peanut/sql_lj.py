from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from core.apps import app
from core.config import config

import pymysql

pymysql.install_as_MySQLdb()
users = config.DB_CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = str(
    users["datatype"] + '://' + users['username'] + ':' + users['password'] + '@' + users['host'] + '/' + users[
        'database'])


print(app.config.get("SQLALCHEMY_DATABASE_URI"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 花生网
class Bj5i5j(db.Model):
    __tablename__ = 'lj'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(1000), nullable=False)  # 区
    house = db.Column(db.String(1000), nullable=False)  # 房子位置
    monthly = db.Column(db.Integer, nullable=False)  # 月租 int
    house_info = db.Column(db.String(1000), nullable=False)  # 房子信息
    agent = db.Column(db.String(1000), nullable=False)  # 房产经纪人
    imgs = db.Column(db.String(1000), nullable=False)  # 房间图片

    def __init__(self, district, house, monthly, house_info, agent, imgs):
        self.district = district
        self.house = house
        self.monthly = monthly
        self.house_info = house_info
        self.agent = agent
        self.imgs = imgs


#
# 添加数据
def add_house(district, house, monthly, house_info, agent, imgs):
    res = Bj5i5j(district, house, monthly, house_info, agent, imgs)
    # print(res)
    print('5i6j')
    db.session.add(res)
    db.session.commit()
    return True


# 显示全部
def query_all():
    res = Bj5i5j.query.all
    return tuple(res())


# 查询图片
def query_img():
    tuple1 = ()
    res = Bj5i5j.query.all
    for i in res():
        tuple1 += (i.imgs,)
    # print(tuple1)
    return tuple1


# query_img()
# print(query_all())
# 查询位置
def query_house():
    tuple1 = ()
    res = Bj5i5j.query.all
    for i in res():
        tuple1 += (i.house,)
    # print(tuple1)
    return tuple1


# query_house()
def query_houseid():
    tuple1 = ()
    res = Bj5i5j.query.all
    for i in res():
        tuple1 += (i.id,)
    # print(tuple1)
    return tuple1


# 房子信息
def query_houseinfo():
    tuple1 = ()
    res = Bj5i5j.query.all
    for i in res():
        tuple1 += (i.house_info,)
    # print(tuple1)
    return tuple1


# query_houseinfo()


# 查月租
def query_housemonthly():
    tuple1 = ()
    res = Bj5i5j.query.all
    for i in res():
        tuple1 += (i.monthly,)
    # print(tuple1)
    return tuple1


# 根据 网站 查询
def query_by_web(web):
    res = Bj5i5j.query.filter_by(web=web).all()
    if res != []:
        return tuple(res)


# 根据 区 查询
def query_by_district(district):
    res = Bj5i5j.query.filter_by(district=district).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)


# 根据 id 查询
def query_by_id(id):
    res = Bj5i5j.query.filter_by(id=id).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)


# 模糊查询 小区名
def query_by_likehouse(house):
    res = Bj5i5j.query.filter(Bj5i5j.house.like("%" + house + "%") if house is not None else "").all()
    # print(res)
    # for i in res:
    #     print(i.house)
    return tuple(res)


# query_by_likehouse('双桥')
# query_by_likehouse('中关村')

# 模糊查询 地铁名
def query_by_liketraffic(traffic):
    res = Bj5i5j.query.filter(Bj5i5j.traffic.like("%" + traffic + "%") if traffic is not None else "").all()
    # print(res)
    if res != []:
        return tuple(res)


# print(query_by_liketraffic('aaa地铁站'))


# 模糊查询 all
def query_likeall(input):
    res = Bj5i5j.query.filter(or_(
        Bj5i5j.district.like("%" + input + "%") if input is not None else "",
        Bj5i5j.house.like("%" + input + "%") if input is not None else "",
        Bj5i5j.monthly.like("%" + input + "%") if input is not None else "",
        Bj5i5j.house_info.like("%" + input + "%") if input is not None else "",
        Bj5i5j.traffic.like("%" + input + "%") if input is not None else "")).all()
    # print(res)
    if res != []:
        return tuple(res)


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
