from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from PShop.models import *
from PShop.views import set_password, valid_user
from Buyer.models import *
import time
from django.views.decorators.cache import cache_page


@cache_page(60*5)
def index(request):
    type_list = GoodsType.objects.all()
    result = [{t.name: t.goods_set.all(), 'pic': t.picture} for t in type_list]
    return render(request, 'buyer/index.html', locals())


def list(request):
    search_goods = request.GET.get('search_goods')
    id = request.GET.get('id')
    goods_list = Goods.objects.all()
    if search_goods:
        goods_list = Goods.objects.filter(name__contains=search_goods)
    if id:
        goods_type = GoodsType.objects.get(id=int(id))
        goods_list = goods_type.goods_set.all()
    return render(request, 'buyer/list.html', {'goods_list': goods_list})


def goods(request, id):
    goods_msg = Goods.objects.get(id=int(id))
    email = request.COOKIES.get('email')
    if email:
        now_data = History.objects.filter(user_email=email).order_by('id')
        if len(now_data) >= 5:
            now_data[0].delete()
        history = History()
        history.user_email = email
        history.goods_id = id
        history.goods_name = goods_msg.name
        history.goods_picture = goods_msg.picture
        history.goods_price = goods_msg.price
        history.save()
    return render(request, 'buyer/goods.html', locals())


def login_valid(fun):
    def inner(request, *args, **kwargs):
        referer = request.GET.get('referer')
        email_cookie = request.COOKIES.get('email')
        id_cookie = request.COOKIES.get('user_id')
        email_session = request.session.get('email')
        if email_cookie and id_cookie and email_session and email_cookie == email_session:
            return fun(request, *args, **kwargs)
        else:
            login_url = '/Buyer/login/'
            if referer:
                login_url = '/Buyer/login/?referer=%s' % referer
            return HttpResponseRedirect(login_url)

    return inner


@login_valid
def cart(request):
    user = request.COOKIES.get('email')
    goods_list = BuyCar.objects.filter(car_user=user)
    num = len(goods_list)
    if request.method == 'POST':
        data = request.POST
        post_data = []
        for key in data:
            if key.startswith('check'):
                id = key.split('_')[1]
                num = 'number_%s' % id
                number = data[num]
                post_data.append((id, number))

        p_order = Pay_order()
        p_order.order_id = str(time.time()).replace('.', '')
        p_order.order_number = len(post_data)
        p_order.order_user = User.objects.get(email=request.COOKIES.get('email'))
        p_order.save()

        order_total = 0

        for id, number in post_data:
            number = int(number)
            goods = Goods.objects.get(id=int(id))
            o_info = Order_info()
            o_info.order_id = p_order
            o_info.goods_name = goods.name
            o_info.goods_number = number
            o_info.goods_price = goods.price
            o_info.goods_total = number * goods.price
            o_info.goods_picture = goods.picture.url
            o_info.order_store = goods.goods_store
            o_info.save()
            order_total += o_info.goods_total
        p_order.order_total = order_total
        p_order.save()
        return HttpResponseRedirect('/Buyer/place_order/?order_id=%s' % p_order.order_id)
    return render(request, 'buyer/cart.html', locals())


def login(request):
    referer = request.GET.get('referer')
    if not referer:
        referer = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = valid_user(email)
        if user:
            post_password = set_password(password)
            db_password = user.password
            if post_password == db_password:
                referer = request.POST.get('referer')
                if referer in ('http://127.0.0.1:8000/Buyer/login/', "None",'http://127.0.0.1:8000/Buyer/register/'):
                    referer = '/Buyer/'
                response = HttpResponseRedirect(referer)
                response.set_cookie('email', user.email)
                response.set_cookie('user_id', user.id)
                request.session['email'] = user.email
                return response
            else:
                error = '密码错误!'
        else:
            error = '用户名不存在!'
    return render(request, 'buyer/login.html', locals())


def logout(request):
    response = HttpResponseRedirect('/Buyer/')
    response.delete_cookie('email')
    response.delete_cookie('user_id')
    request.session.clear()
    return response


def user_valid(user):
    try:
        user_db = User.objects.get(email=user)
    except Exception as e:
        return False
    else:
        return user_db


def register(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_cpassword = request.POST.get('cpassword')
        post_password = set_password(user_password)
        user = User()
        user.email = user_email
        user.password = post_password
        user.save()
        return HttpResponseRedirect('/Buyer/login/')
    return render(request, 'buyer/register.html', locals())


def valid_email(request):
    if request.method == 'GET':
        user_email = request.GET.get('get_email')
        re_data = []
        if user_valid(user_email):
            re_data.append({'re': 'True'})
        else:
            re_data.append({'re': 'False'})
        return JsonResponse({'re_data': re_data})


@login_valid
def add_car(request):
    result = {'state': 'error', 'data': ''}
    if request.method == 'POST':
        user = request.COOKIES.get('email')
        goods_id = request.POST.get('goods_id')
        number = request.POST.get('number', 1)
        try:
            goods = Goods.objects.get(id=goods_id)
        except Exception as e:
            result['data'] = str(e)
        else:
            car = BuyCar()
            car.car_user = user
            car.goods_name = goods.name
            car.goods_picture = goods.picture
            car.goods_price = goods.price
            car.goods_number = number
            car.goods_total = int(number) * goods.price
            car.goods_store = goods.goods_store.id
            car.goods_id = goods.id
            car.save()
            result['state'] = 'susses'
            result['data'] = '加入购物车成功'
    return JsonResponse(result)


# def pay_order(request):
#
#     return render(request, 'buyer/place_order.html', locals())


def place_order(request):
    user_email = request.COOKIES.get('email')
    addr = GoodsAddress.objects.filter(user_email=user_email)
    order_id = request.GET.get('order_id')
    if order_id:
        p_order = Pay_order.objects.get(order_id=order_id)
        order_info = p_order.order_info_set.all()
    return render(request, 'buyer/place_order.html', locals())

@login_valid
def user_center_info(request):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    addr = GoodsAddress.objects.get(state=1)
    goods_list = History.objects.filter(user_email=user_email)
    return render(request, 'buyer/user_center_info.html', locals())

@login_valid
def user_center_site(request):
    email = request.COOKIES.get('email')
    user_data = User.objects.get(email=email)
    try:
        addr = user_data.goodsaddress_set.filter(state=1)[0]
    except Exception as e:
        error = '暂无地址信息'
    if request.method == 'POST':
        recv = request.POST.get('recv')
        address = request.POST.get('address')
        post_number = request.POST.get('post_number')
        phone = request.POST.get('phone')
        addr = GoodsAddress()
        addr.recver = recv
        addr.address = address
        addr.post_number = post_number
        addr.phone = phone
        addr.state = 0
        addr.user_email = user_data.email
        addr.all_address = user_data
        addr.save()
    return render(request, 'buyer/user_center_site.html', locals())


@login_valid
def user_center_order(request):
    email = request.COOKIES.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        order_list = user.pay_order_set.all()
    return render(request, 'buyer/user_center_order.html', locals())

def middle_test(request):
    def hello():
        return HttpResponseRedirect('hello world')
    rep = HttpResponse('你好')
    rep.render = hello
    return rep
