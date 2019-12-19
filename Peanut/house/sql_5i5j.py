from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'basetype://username:password@host:port/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 北京市
class Bj5i5j(db.Model):
    __tablename__ = 'Bj5i5j'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(20), nullable=False)  # 区
    house = db.Column(db.String(20), nullable=False)  # 房子位置
    monthly = db.Column(db.Integer, nullable=False)  # 月租 int
    house_info = db.Column(db.String(80), nullable=False)  # 房子信息
    agent = db.Column(db.String(20), nullable=False)  # 房产经纪人
    imgs = db.Column(db.String(80), nullable=False)  # 房间图片
    chum = db.Column(db.String(80), nullable=False)  # 室友
    traffic = db.Column(db.String(80), nullable=False)  # 交通
    property_fee = db.Column(db.String(20), nullable=False)  # 物业费

    def __init__(self, district, house, monthly, house_info, agent, imgs, chum, traffic, property_fee):
        self.district = district
        self.house = house
        self.monthly = monthly
        self.house_info = house_info
        self.agent = agent
        self.imgs = imgs
        self.chum = chum
        self.traffic = traffic
        self.property_fee = property_fee


# 添加数据
def add_house(district, house, monthly, house_info, agent, imgs, chum, traffic, property_fee):
    res = Bj5i5j(district, house, monthly, house_info, agent, imgs, chum, traffic, property_fee)
    print(res)
    db.session.add(res)
    db.session.commit()
    return True


# print(add_house('朝阳', '双桥双桥小区3居室主卧', 1900, '呼呼呼', '程雷18519314699', '呼呼呼', '急急急', '距八通线双桥地铁站A口1618米', '小区物业费1元/平米/月'))

# 显示全部
def query_all():
    res = Bj5i5j.query.all
    return tuple(res())


# print(query_all())


# 根据 区 查询
def query_by_district(district):
    res = Bj5i5j.query.filter_by(district=district).all()
    if res != []:
        return tuple(res)

# query_by_district('朝阳')
# query_by_district('朝')


# 创建表(全部)
# db.create_all()
