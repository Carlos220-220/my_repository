from django.shortcuts import render_to_response


def index(request):
    title_list = [
        {'title': '首页', 'class': 'nav-active', 'href':'/index/'},
        {'title': '品牌故事', 'href':'/pinpai/'},
        {'title': '美食系列', 'href':'/meishi/'},
        {'title': '店面展示', 'href':'/shop/'},
        {'title': '新闻资讯', 'href':'/news/'},
        {'title': '关于我们', 'href':'/about-us/'},
    ]

    food_list1 = [
        {'food': '茶漱海鲜汤', 'class_a': 'newfood-p1',
         'class_l': 'newfood-right newfood-li1'},
        {'food': '玉米海螺沟', 'class_a': 'newfood-p2',
         'class_l': 'newfood-right newfood-li2'},
        {'food': '芝士蛋糕卷', 'class_a': 'newfood-p3',
         'class_l': 'newfood-right newfood-li3'},
        {'food': '芝士大虾', 'class_a': 'newfood-p4',
         'class_l': 'newfood-li4'},
        {'food': '西冷牛排', 'class_a': 'newfood-p5',
         'class_l': 'newfood-right newfood-li5'},
        {'food': '草莓布丁杯', 'class_a': 'newfood-p6',
         'class_l': 'newfood-right newfood-li6'},
        {'food': '蜂蜜布丁', 'class_a': 'newfood-p7',
         'class_l': 'newfood-right newfood-li7'},
        {'food': '墨西哥牛排', 'class_a': 'newfood-p8',
         'class_l': 'newfood-li8'},
    ]

    food_list2 = [
        {'food': '玉米海螺沟', 'class_a': 'newfood-p2',
         'class_l': 'newfood-right newfood-li2'},
        {'food': '芝士大虾', 'class_a': 'newfood-p4',
         'class_l': 'newfood-right newfood-li4'},
        {'food': '草莓布丁杯', 'class_a': 'newfood-p6',
         'class_l': 'newfood-right newfood-li6'},
        {'food': '墨西哥牛排', 'class_a': 'newfood-p8',
         'class_l': 'newfood-li8'},
        {'food': '茶漱海鲜汤', 'class_a': 'newfood-p1',
         'class_l': 'newfood-right newfood-li1'},
        {'food': '芝士蛋糕卷', 'class_a': 'newfood-p3',
         'class_l': 'newfood-right newfood-li3'},
        {'food': '西冷牛排', 'class_a': 'newfood-p5',
         'class_l': 'newfood-right newfood-li5'},
        {'food': '蜂蜜布丁', 'class_a': 'newfood-p7',
         'class_l': 'newfood-li7'},
    ]

    food_list3 = [
        {'food': '西冷牛排', 'class_a': 'newfood-p5',
         'class_l': 'newfood-right newfood-li5'},
        {'food': '茶漱海鲜汤', 'class_a': 'newfood-p1',
         'class_l': 'newfood-right newfood-li1'},
        {'food': '芝士蛋糕卷', 'class_a': 'newfood-p3',
         'class_l': 'newfood-right newfood-li3'},
        {'food': '玉米海螺沟', 'class_a': 'newfood-p2',
         'class_l': 'newfood-li2'},
        {'food': '蜂蜜布丁', 'class_a': 'newfood-p7',
         'class_l': 'newfood-right newfood-li7'},
        {'food': '草莓布丁杯', 'class_a': 'newfood-p6',
         'class_l': 'newfood-right newfood-li6'},
        {'food': '墨西哥牛排', 'class_a': 'newfood-p8',
         'class_l': 'newfood-right newfood-li8'},
        {'food': '芝士大虾', 'class_a': 'newfood-p4',
         'class_l': 'newfood-li4'},
    ]

    text_list1 = [
        {'text': '贵族食代牛排是昔日的台湾首富、台湾知名企业贵族食代集团董事长王永庆先生招待贵宾的知名私房料理。严选一头牛的第六至第八对肋骨这六块牛排。是以“一头牛仅供6客”的贵族食代牛排为招牌菜的中高价位直营连锁西餐厅，独具中国口味，全熟牛排，鲜嫩多汁，适合中国人口味，以菜色精致、好吃、服务好、风格高雅、管理专业着称。'},
        {'text': '何谓经典，可能就是在品鉴无数美食后，其绝妙的滋味仍旧不能被替代。再次品味时，仍能激起内心的波澜与感动。如此经典，我们将为您重新诠释。全新的摆盘，搭配特制爽口的配菜，全熟风味，您不可辜负的舌尖美味。'},
        {'text': '2003年登陆大陆，截至目前，贵族食代牛排在上海、北京、深圳、广州、南京、武汉、成都、重庆等地已经有40余家直营店，成为高端连锁牛排的领导品牌。'}
    ]

    text_list2 = [
        {'text': '贵族食代牛排东莞厚街万达餐厅开业', 'time': '2016-09-28'},
        {'text': '贵族食代牛排无锡大成巷餐厅开业', 'time': '2016-09-23'},
        {'text': '贵族食代牛排武汉黄陂广场餐厅开业', 'time': '2016-09-20'},
        {'text': '贵族食代牛排福州永嘉天地餐厅开业', 'time': '2016-09-17'},
        {'text': '贵族食代牛排网络大学第一批“学霸”亮相', 'time': '2016-09-14'},
        {'text': '华南市场2016半年度餐厅经理营运会召开', 'time': '2016-09-05'},
        {'text': '浙江大区召开餐厅经理营运会议', 'time': '2016-09-23'},
        {'text': '贵族食代牛排武汉武商众圆餐厅开业', 'time': '2016-09-15'},
    ]

    link_list = [
        {'num': '6'},
        {'num': '5'},
        {'num': '4'},
        {'num': '3'},
        {'num': '2'},
        {'num': '1'},
    ]

    text_list3 = [
        {'text': 'CopyRight©2003-2015 www.91cy.cn All rigt rederved'},
        {'text': '版权所有：贵族食代牛排有限公司'},
        {'text': 'ICP备案号：京ICP备16047255号-3本站信息由会员自主添加，如信息涉及隐私等，网站不承担任何责任！'},
    ]

    return render_to_response("index.html", locals())


def pinpai(request):
    return render_to_response("pinpai.html", locals())

def meishi(request):
    return render_to_response("meishi.html", locals())

def shop(request):
    return render_to_response("shop.html", locals())

def news(request):
    return render_to_response("news.html", locals())

def about_us(request):
    return render_to_response("about-us.html", locals())

def meishi_con(request):
    return render_to_response("meishi-con.html", locals())

def news_com(request):
    return render_to_response("news-con.html", locals())

def shop_con(request):
    return render_to_response("shop-con.html", locals())