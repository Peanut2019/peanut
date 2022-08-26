from flask import render_template, request, url_for, redirect
from core.apps import app
import sql_lj, peanut_form, sql_zuke


# 404处理
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


# 500处理
@app.errorhandler(500)
def servererror(e):
    return render_template('500.html'), 500


# 首页
@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = peanut_form.MyFrom()
    if request.method == "GET":
        lj_images = sql_lj.query_img()
        lj_house = sql_lj.query_house()  # wz
        lj_houseinfo = sql_lj.query_houseinfo()  # 房子xx
        lj_houseid = sql_lj.query_houseid()  # 房子id
        ljlen = len(lj_images)

        zk_images = sql_zuke.query_img()  # 租客网图片
        zk_house = sql_zuke.query_house()  # 租客网房源位置
        zk_houseinfo = sql_zuke.query_houseinfo()  # 租客网房信息
        zk_houseid = sql_zuke.query_houseid()  # 查id
        zklen = len(zk_images)

        return render_template('home_page.html', images=lj_images, form=form, zrimg=zk_images,
                               ljhouse=lj_house, zkhouse=zk_house,
                               lj_houseinfo=lj_houseinfo, lj_houseid=lj_houseid, zk_houseinfo=zk_houseinfo,
                               zk_houseid=zk_houseid,
                               ljlen=ljlen, zklen=zklen)
    else:
        if form.validate_on_submit():
            url_args = request.form['title']
            return redirect(url_for('pageinfo_', searchs=url_args))


# 搜索后的界面
@app.route('/pageinfo/<searchs>', methods=["GET", "POST"])
def pageinfo_(searchs):
    house = []
    houseinfo = []
    images = []
    webid = []
    zksearch = sql_zuke.query_likeall(searchs)  # 租客
    if zksearch != None:
        searchlen = len(zksearch)
        for le in range(searchlen):
            zkhouse = zksearch[le].house  # 位置
            zkhouseinfo = zksearch[le].house_info  # 信息
            zkimgs = zksearch[le].imgs  # 图片
            zkid = zksearch[le].id  # id
            house.append(zkhouse)
            houseinfo.append(zkhouseinfo)
            images.append(zkimgs)
            webid.append(zkid)
    # dksearch = sql_danke.query_likeall(searchs)  # danke
    # if dksearch != None:
    #     searchlen = len(dksearch)
    #     for le in range(searchlen):
    #         dkhouse = dksearch[le].house  # 位置
    #         dkhouseinfo = dksearch[le].house_info  # 信息
    #         dkimgs = dksearch[le].imgs  # 图片
    #         dkid = dksearch[le].id  # id
    #         house.append(dkhouse)
    #         houseinfo.append(dkhouseinfo)
    #         images.append(dkimgs)
    #         webid.append(dkid)

    # ljsearch = sql_danke.query_likeall(searchs)  # danke
    # if ljsearch != None:
    #     searchlen = len(ljsearch)
    #     for le in range(searchlen):
    #         ljhouse = ljsearch[le].house  # 位置
    #         ljhouseinfo = ljsearch[le].house_info  # 信息
    #         ljimgs = ljsearch[le].imgs  # 图片
    #         ljid = ljsearch[le].id  # id
    #         house.append(ljhouse)
    #         houseinfo.append(ljhouseinfo)
    #         images.append(ljimgs)
    #         webid.append(ljid)

    if house == []:
        return render_template('404.html')
    return render_template('regions_info.html', house=house, searchs=searchs, houseinfo=houseinfo, images=images,
                           webid=webid)


# 点击平台之后的页面
@app.route('/terrace/<name>')
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
@app.route('/region/<district>/')
def regions(district):
    house = []
    houseinfo = []
    images = []
    webid = []
    # dkhome = sql_danke.query_by_district(district)  # 蛋壳
    # if dkhome != None:
    #     reslen = len(dkhome)
    #     for le in range(reslen):
    #         dkhouse = dkhome[le].house  # 位置
    #         dkhouse_info = dkhome[le].house_info  # 信息
    #         dkimgs = dkhome[le].imgs  # 图片
    #         dkid = dkhome[le].id  # id
    #
    #         house.append(dkhouse)
    #         houseinfo.append(dkhouse_info)
    #         images.append(dkimgs)
    #         webid.append(dkid)

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
@app.route('/houseinfo/<table>/<int:hostid>')
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
        # elif table == 'sql_danke':
        #     dkid = sql_danke.query_by_id(hostid)
        #     house_dk = dkid[0].house  # 房子位置
        #     monthly_dk = dkid[0].monthly  # 租金
        #     houseinfo_dk = dkid[0].house_info  # 房子信息
        #     cfg_dk = dkid[0].cfg  # 配置
        #     chum_dk = dkid[0].chum  # 室友
        #     traffic_dk = dkid[0].traffic  # 交通
        #     imgs_dk = dkid[0].imgs  # 图片
        #     img = imgs_dk.split(' ')
        #     return render_template('dkhouse_info.html', house_dk=house_dk, monthly_dk=monthly_dk,
        #                            houseinfo_dk=houseinfo_dk, cfg_dk=cfg_dk, chum_dk=chum_dk,
        #                            traffic_dk=traffic_dk, imgs_dk=img)
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


if __name__ == '__main__':
    app.run(debug=True)
