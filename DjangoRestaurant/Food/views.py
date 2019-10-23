from rest_framework import mixins, viewsets
from Food.models import *
from django.http import HttpResponse
import random
from Food.serializers import FoodSerializers
from django.shortcuts import render

class Foods_View(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Foods.objects.all()
    serializer_class = FoodSerializers

def add_foods_type(request):
    type_list = [
        '经典牛排', '意面/烩饭', '风味披萨', '甜品小食', '酒水饮料', '其他',
    ]
    for types in type_list:
        ft = FoodsType()
        ft.label = types
        ft.description = '%s好吃不贵' % types
        # ft.save()

    return HttpResponse('菜品种类添加成功')


def add_foods(request):
    foods = [
        '茶漱海鲜汤', '玉米海螺沟', '芝士蛋糕卷', '芝士大虾',
        '西冷牛排', '草莓布丁杯', '蜂蜜布丁', '墨西哥牛排',
    ]
    for foods in foods:
        f = Foods()
        f.name = foods
        f.price = random.randint(1, 400)
        f.picture = '1.jpg'
        f.description = '%s 好吃,有点小贵' % foods
        f.type_id = FoodsType.objects.get(id=random.randint(1, 6))
        # f.save()
    return HttpResponse('菜品添加成功')


def add_news(request):
    address = [
        '石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番',
        '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯',
        '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏'
    ]
    for i in range(100):
        news = News()
        news.title = '贵族食代牛排%s餐厅开业' % random.choice(address)
        news.time = '%d-%d-%d' % (
            random.randint(2012, 2019),
            random.randint(1, 12),
            random.randint(1, 31)
        )
        news.description = news.title * 10
        news.image = '1.jpg'
        news.content = news.title * 50
        news.type = '新闻资讯'
        # news.save()
    return HttpResponse('新闻添加成功')


def add_shop(request):
    address = [
        '石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番',
        '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯',
        '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏'
    ]
    for i in range(100):
        shop = Shop()
        shop.name = '贵族食代牛排%s餐厅' % random.choice(address)
        shop.picture = '1.jpg'
        shop.open_time = '上午10:00-13:00 下午16:00'
        shop.address = random.choice(address)
        shop.label = '法国菜,有包间,有车位,可刷卡,崇文区,地铁1号线,地铁2号线,' \
                     '地铁5号线,崇文门外大街,前门总医院,天坛,祈年殿,龙潭湖公园,' \
                     '北京体育馆,中央戏剧学院,崇文区儿童医院,新世界商场,北京站,' \
                     '新闻大厦,北京饭店,北京市政府,东交民巷,天安门,朋友聚会,' \
                     '家人就餐,谈情约会'
        # shop.save()
        for i in range(random.randint(6, 8)):
            shop.foods_id.add(
                Foods.objects.get(id=random.randint(1, 8))
            )
            # shop.save()
    return HttpResponse('店铺添加成功')


def add_company(request):
    address1 = [
        '石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番',
        '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯',
        '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏'
    ]
    for i in range(100):
        c = Company()
        c.name = '%s分公司' % random.choice(address1)
        c.picture = '1.jpg'
        c.phone = '0512-%d %d' % (
            random.randint(1000, 9999),
            random.randint(1000, 9999),
        )
        c.fax = '0512-%d %d' % (
            random.randint(1000, 9999),
            random.randint(1000, 9999),
        )
        c.post_code = '%d' % random.randint(100000, 999999)
        c.address = ('%s' % random.choice(address1)) * 10
        # c.save()
    return HttpResponse('公司添加成功')

def meishi(request):
    return render(request, 'meishi.html', locals())
