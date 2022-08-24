from sqlalchemy import or_
from sql_lj import db


# 花生网
class Zkweb(db.Model):
    __tablename__ = 'zk'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(1000), nullable=False)  # 区
    house = db.Column(db.String(1000), nullable=False)  # 房子位置
    monthly = db.Column(db.String(1000), nullable=False)  # 月租 int
    house_info = db.Column(db.String(1000), nullable=False)  # 房子信息
    agent = db.Column(db.String(1000), nullable=False)  # 房产经纪人
    imgs = db.Column(db.String(1000), nullable=False)  # 房间图片
    traffic = db.Column(db.String(1000), nullable=False)  # 交通
    property_fee = db.Column(db.String(1000), nullable=False)  # 物业费

    def __init__(self, district, house, monthly, house_info, agent, imgs, traffic, property_fee):
        self.district = district
        self.house = house
        self.monthly = monthly
        self.house_info = house_info
        self.agent = agent
        self.imgs = imgs
        self.traffic = traffic
        self.property_fee = property_fee


#
# 添加数据
def add_house(district, house, monthly, house_info, agent, imgs, traffic, property_fee):
    res = Zkweb(district, house, monthly, house_info, agent, imgs, traffic, property_fee)
    # print(res)
    # print('5i6j')
    db.session.add(res)
    db.session.commit()
    return True


# 显示全部
def query_all():
    res = Zkweb.query.all
    return tuple(res())


# 查询图片
def query_img():
    tuple1 = ()
    res = Zkweb.query.all
    for i in res():
        tuple1 += (i.imgs,)
    # print(tuple1)
    return tuple1


# query_img()
# print(query_all())
# 查询位置
def query_house():
    tuple1 = ()
    res = Zkweb.query.all
    for i in res():
        tuple1 += (i.house,)
    # print(tuple1)
    return tuple1


# query_house()
def query_houseid():
    tuple1 = ()
    res = Zkweb.query.all
    for i in res():
        tuple1 += (i.id,)
    # print(tuple1)
    return tuple1


# 房子信息
def query_houseinfo():
    tuple1 = ()
    res = Zkweb.query.all
    for i in res():
        tuple1 += (i.house_info,)
    # print(tuple1)
    return tuple1


# query_houseinfo()


# 查月租
def query_housemonthly():
    tuple1 = ()
    res = Zkweb.query.all
    for i in res():
        tuple1 += (i.monthly,)
    # print(tuple1)
    return tuple1


# 根据 网站 查询
def query_by_web(web):
    res = Zkweb.query.filter_by(web=web).all()
    if res != []:
        return tuple(res)


# 根据 区 查询
def query_by_district(district):
    res = Zkweb.query.filter_by(district=district).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)


# print(query_by_district('西城区'))
#
# 根据 id 查询
def query_by_id(id):
    res = Zkweb.query.filter_by(id=id).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)


# 模糊查询 小区名
def query_by_likehouse(house):
    res = Zkweb.query.filter(Zkweb.house.like("%" + house + "%") if house is not None else "").all()
    # print(res)
    # for i in res:
    #     print(i.house)
    return tuple(res)


# query_by_likehouse('双桥')
# query_by_likehouse('中关村')

# 模糊查询 地铁名
def query_by_liketraffic(traffic):
    res = Zkweb.query.filter(Zkweb.traffic.like("%" + traffic + "%") if traffic is not None else "").all()
    # print(res)
    if res != []:
        return tuple(res)


# print(query_by_liketraffic('aaa地铁站'))


# 模糊查询 all
def query_likeall(input):
    res = Zkweb.query.filter(or_(
        Zkweb.district.like("%" + input + "%") if input is not None else "",
        Zkweb.house.like("%" + input + "%") if input is not None else "",
        Zkweb.monthly.like("%" + input + "%") if input is not None else "",
        Zkweb.house_info.like("%" + input + "%") if input is not None else "",
        Zkweb.traffic.like("%" + input + "%") if input is not None else "")).all()
    # print(res)
    if res != []:
        return tuple(res)


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()