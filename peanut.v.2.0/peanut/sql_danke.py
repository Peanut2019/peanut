from sqlalchemy import or_
from sql_lj import db

# 花生网
class Bjdanke(db.Model):
    __tablename__ = 'Bjdanke'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(1000), nullable=False)  # 区
    house = db.Column(db.String(1000), nullable=False)  # 房子位置
    monthly = db.Column(db.Integer, nullable=False)  # 月租 int
    house_info = db.Column(db.String(1000), nullable=False)  # 房子信息
    cfg = db.Column(db.String(1000), nullable=False)  # 房间配置
    imgs = db.Column(db.String(1000), nullable=False)  # 房间图片
    chum = db.Column(db.String(1000), nullable=True)  # 室友
    traffic = db.Column(db.String(1000), nullable=False)  # 交通

    def __init__(self, district, house, monthly, house_info, cfg, imgs,chum, traffic):
        self.district = district
        self.house = house
        self.monthly = monthly
        self.house_info = house_info
        self.cfg = cfg
        self.imgs = imgs
        self.chum = chum
        self.traffic = traffic


# 创建表(全部)
# db.create_all()
# print('546546')

# db.drop_all()

# 添加数据
def add_house(district, house, monthly, house_info, cfg, imgs, traffic, chum):
    res = Bjdanke(district, house, monthly, house_info, cfg, imgs, traffic, chum)
    # print(res)
    # print('danke')
    db.session.add(res)
    db.session.commit()
    return True



# 显示全部
def query_all():
    res = Bjdanke.query.all
    return tuple(res())

#查找图片
def query_img():
    tuple1 = ()
    res = Bjdanke.query.all
    for i in res():
        tuple1 += (i.imgs,)
    # print(tuple1)
    return tuple1

#查询位置
def query_house():
    tuple1 = ()
    res = Bjdanke.query.all
    for i in res():
        tuple1 += (i.house,)
    # print(tuple1)
    return tuple1
# query_house()

# print(query_all())

#房子信息
def query_houseinfo():
    tuple1 = ()
    res = Bjdanke.query.all
    for i in res():
        tuple1 += (i.house_info,)
    # print(tuple1)
    return tuple1

#查月租
def query_housemonthly():
    tuple1 = ()
    res = Bjdanke.query.all
    for i in res():
        tuple1 += (i.monthly,)
    # print(tuple1)
    return tuple1


# 根据 月租 查询
def query_by_web(monthly):
    res = Bjdanke.query.filter_by(monthly=monthly).all()
    if res != []:
        return tuple(res)


# 根据 区 查询
def query_by_district(district):
    res = Bjdanke.query.filter_by(district=district).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)

# 根据 id 查询
def query_by_id(id):
    res = Bjdanke.query.filter_by(id=id).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)

def query_houseid():
    tuple1 = ()
    res = Bjdanke.query.all
    for i in res():
        tuple1 += (i.id,)
    # print(tuple1)
    return tuple1

# 模糊查询 小区名
def query_by_likehouse(house):
    res = Bjdanke.query.filter(Bjdanke.house.like("%" + house + "%") if house is not None else "").all()
    # print(res)
    # for i in res:
    #     print(i.house)
    return tuple(res)


# query_by_likehouse('双桥')
# query_by_likehouse('中关村')

# 模糊查询 地铁名
def query_by_liketraffic(traffic):
    res = Bjdanke.query.filter(Bjdanke.traffic.like("%" + traffic + "%") if traffic is not None else "").all()
    # print(res)
    if res != []:
        return tuple(res)





# 模糊查询 all
def query_likeall(input):
    res = Bjdanke.query.filter(or_(
        Bjdanke.district.like("%" + input + "%") if input is not None else "",
        Bjdanke.house.like("%" + input + "%") if input is not None else "",
        Bjdanke.monthly.like("%" + input + "%") if input is not None else "",
        Bjdanke.house_info.like("%" + input + "%") if input is not None else "",
        Bjdanke.traffic.like("%" + input + "%") if input is not None else "")).all()
    # print(res)
    if res != []:
        return tuple(res)

