from flask import render_template, request, url_for, redirect
from flask.blueprints import Blueprint
import sql_lj, peanut_form, sql_zuke

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET', 'POST'])
def homepage():
    form = peanut_form.MyFrom()
    if request.method == "GET":
        lj_images = sql_lj.query_img()
        lj_house = sql_lj.query_house()  # wz
        lj_house_info = sql_lj.query_houseinfo()  # 房子xx
        lj_house_id = sql_lj.query_houseid()  # 房子id
        lj_img_count = len(lj_images)

        zk_images = sql_zuke.query_img()  # 租客网图片
        zk_house = sql_zuke.query_house()  # 租客网房源位置
        zk_houseinfo = sql_zuke.query_houseinfo()  # 租客网房信息
        zk_houseid = sql_zuke.query_houseid()  # 查id
        zklen = len(zk_images)

        return render_template('home_page.html', images=lj_images, form=form, zrimg=zk_images,
                               ljhouse=lj_house, zkhouse=zk_house,
                               lj_houseinfo=lj_house_info, lj_houseid=lj_house_id, zk_houseinfo=zk_houseinfo,
                               zk_houseid=zk_houseid,
                               ljlen=lj_img_count, zklen=zklen)
    else:
        if form.validate_on_submit():
            url_args = request.form['title']
            return redirect(url_for('pageinfo_', searchs=url_args))


# 搜索后的界面
@index_bp.route('/pageinfo/<searchs>', methods=["GET", "POST"])
def pageinfo_(searchs):
    house = []
    # house_info = []
    images = []
    web_id = []
    zk_search = sql_zuke.query_likeall(searchs)  # 租客
    if zk_search:
        search_len = len(zk_search)
        for le in range(search_len):
            zkhouse = zk_search[le].house  # 位置
            zkhouseinfo = zk_search[le].house_info  # 信息
            zkimgs = zk_search[le].imgs  # 图片
            zkid = zk_search[le].id  # id
            house.append(zkhouse)
            houseinfo.append(zkhouseinfo)
            images.append(zkimgs)
            web_id.append(zkid)

    if not house:
        return render_template('404.html')
    return render_template('regions_info.html', house=house, searchs=searchs, houseinfo=houseinfo, images=images,
                           webid=web_id)


# 点击平台之后的页面
@index_bp.route('/terrace/<name>')
def terraces(name):
    terrace = request.args.get('terrace')  # 获取平台名
    terrace = terrace[1:-1]
    if terrace == '租客网':
        zk_images = sql_zuke.query_img()  # 租客网图片
        zk_house = sql_zuke.query_house()  # 租客网房源位置
        zk_houseinfo = sql_zuke.query_houseinfo()  # 租客网房信息
        zk_houseid = sql_zuke.query_houseid()  # 查id
        zklen = len(zk_images)
        return render_template('terraced_zk.html', zk_images=zk_images, zk_house=zk_house, zk_houseinfo=zk_houseinfo,
                               zk_houseid=zk_houseid, zklen=zklen, terrace=terrace)
    if terrace == '链家':
        lj_images = sql_lj.query_img()  # tp
        lj_house = sql_lj.query_house()  # wz
        lj_houseinfo = sql_lj.query_houseinfo()  # 房子xx
        lj_houseid = sql_lj.query_houseid()  # 房子id
        ljlen = len(lj_house)
        ljimage = list(lj_images)

        return render_template('terraced_lj.html', terrace=terrace, lj_images=ljimage, lj_house=lj_house,
                               lj_houseinfo=lj_houseinfo, lj_houseid=lj_houseid, ljlen=ljlen)


# 点开区之后的页面
@index_bp.route('/region/<district>/')
def regions(district):
    house = []
    houseinfo = []
    images = []
    webid = []

    zkhome = sql_zuke.query_by_district(district)  # 租客
    if zkhome != None:
        zklen = len(zkhome)

        for le in range(zklen):
            zkhouse = zkhome[le].house  # 位置
            zkhouse_info = zkhome[le].house_info  # 信息
            zkimgs = zkhome[le].imgs  # 图片
            zkid = zkhome[le].id  # id
            house.append(zkhouse)
            houseinfo.append(zkhouse_info)
            images.append(zkimgs)
            webid.append(zkid)

    ljhome = sql_lj.query_by_district(district)  # 链家
    if ljhome != None:
        ljlen = len(ljhome)
        for le in range(ljlen):
            ljhouse = ljhome[le].house  # 位置
            ljhouseinfo = ljhome[le].house_info  # 信息
            ljimgs = ljhome[le].imgs  # 图片
            ljid = ljhome[le].id  # id
            house.append(ljhouse)
            houseinfo.append(ljhouseinfo)
            images.append(ljimgs)
            webid.append(ljid)
    if house == []:
        return render_template('404.html')
    houselen = len(house)

    return render_template('regions_info.html', house=house, houseinfo=houseinfo, images=images, webid=webid,
                           houselen=houselen, district=district)


# 详情页
@index_bp.route('/houseinfo/<table>/<int:hostid>')
def houseinfo(table, hostid):
    if type(hostid) != str:
        if table == 'sql_lj':
            ljid = sql_lj.query_by_id(hostid)
            house = ljid[0].house  # 房子位置
            house_info = ljid[0].house_info  # 房子信息
            house_monthly = ljid[0].monthly  # 月租
            house_agent = ljid[0].agent  # 房子经纪人
            house_img = ljid[0].imgs  # 房子图片
            ljimg = house_img.split(' ')
            return render_template('ljhouse_info.html', house=house, house_info=house_info, house_monthly=house_monthly,
                                   house_agent=house_agent,
                                   house_img=ljimg)
        elif table == 'sql_zuke':
            zkid = sql_zuke.query_by_id(hostid)

            zkhouse = zkid[0].house  # 房子位置
            zkmonthly = zkid[0].monthly  # 月租
            zkhouse_info = zkid[0].house_info  # 房间信息
            zkagent = zkid[0].agent  # 经纪人
            zktraffic = zkid[0].traffic  # 交通
            zkproperty_fee = zkid[0].property_fee  # 物业
            zkimgs = zkid[0].imgs
            img = zkimgs.split(' ')  # 图片
            return render_template('zkhouse_info.html', zkhouse=zkhouse, zkmonthly=zkmonthly, zkhouse_info=zkhouse_info,
                                   zkagent=zkagent, zktraffic=zktraffic, zkproperty_fee=zkproperty_fee, zkimg=img)
