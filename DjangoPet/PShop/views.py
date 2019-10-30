from django.shortcuts import render
from django.http import HttpResponseRedirect
from PShop.models import Goods
from PUser.views import *


# 下发cookie
def login_valid(fun):
    def inner(request, *args, **kwargs):
        email_cookie = request.COOKIES.get('email')
        id_cookie = request.COOKIES.get('user_id')
        email_session = request.session.get('email')
        if email_cookie and id_cookie and email_session and email_cookie == email_session:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/PShop/login/')

    return inner


# 后台卖家注册功能
def register(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_error = ''
        if valid_user(user_email):
            user_error = '当前邮箱已被注册!'
        else:
            post_password = set_password(user_password)
            add_user(email=user_email, password=post_password)
            return HttpResponseRedirect(request, '/PShop/login/')
    return render(request, 'pshop/register.html', locals())


# 后台卖家登陆
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = valid_user(email)
        if user:
            post_password = set_password(password)
            db_password = user.password
            if post_password == db_password:
                response = HttpResponseRedirect('/PShop/')
                response.set_cookie('email', user.email)
                response.set_cookie('user_id', user.id)
                request.session['email'] = user.email
                return response
            else:
                error = '密码错误!'
        else:
            error = '用户名不存在!'
    return render(request, 'pshop/login.html', locals())


@login_valid
def index(request):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    return render(request, 'pshop/index.html', {'user': user})


# 退出登陆
def logout(request):
    response = HttpResponseRedirect('/PShop/login/')
    response.delete_cookie('email')
    response.delete_cookie('user_id')
    request.session.clear()
    return response


def forget_password(request):
    return render(request, 'pshop/forget_password.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and valid_user(email):
            hash_code = set_password(email)
            content = 'http://127.0.0.1:8000/PShop/change_password/?email=%s&token=%s' % (email, hash_code)
            print(content)
    return HttpResponseRedirect('/PShop/forget_password/')


def change_password(request):
    if request.method == 'POST':
        cookie_email = request.COOKIES.get('email')
        session_password = request.POST.get('password')

        e = User.objects.get(email=cookie_email)
        e.password = set_password(session_password)
        e.save()
        return HttpResponseRedirect('/PShop/login/')

    email = request.GET.get('email')
    token = request.GET.get('token')
    now_token = set_password(email)
    if valid_user(email) and now_token == token:
        return render(request, 'pshop/change_password.html')
    else:
        return HttpResponseRedirect('/PShop/forget_password/')


@login_valid
def profile(request):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    return render(request, 'pshop/profile.html', {'user': user})


@login_valid
def set_profile(request):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    if request.method == 'POST':
        post_data = request.POST
        username = post_data.get('username')
        gender = post_data.get('gender')
        age = post_data.get('age')
        phone = post_data.get('phone')
        address = post_data.get('address')
        picture = request.FILES.get('picture')
        user.username = username
        user.gender = gender
        user.age = age
        user.phone = phone
        user.address = address
        if picture:
            user.picture = picture
        user.save()
        return HttpResponseRedirect('/PShop/profile/')
    return render(request, 'pshop/set_profile.html', locals())


def profile_password(request):
    if request.method == 'POST':
        get_email = request.COOKIES.get('email')
        get_password = request.POST.get('password')
        user_email = User.objects.get(email=get_email)
        error = '请输入密码'
        if get_password:
            new_password = set_password(get_password)
            user_email.password = new_password
            user_email.save()
            response = HttpResponseRedirect('/PShop/login/')
            response.delete_cookie('email')
            response.delete_cookie('user_id')
            request.session.clear()
            return response
        else:
            return error

    return render(request, 'pshop/profile.html', locals())


# @login_valid
# def add_goods(request):
#     user_email = request.COOKIES.get('email')
#     user = User.objects.get(email=user_email)
#     if request.method == 'POST':
#         post_data = request.POST
#         name = post_data.get('name')
#         price = post_data.get('price')
#         number = post_data.get('number')
#         production = post_data.get('production')
#         safe_date = post_data.get('safe_date')
#         description = post_data.get('description')
#         picture = request.FILES.get('picture')
#
#
#         goods = Goods()
#         goods.name = name
#         goods.price = price
#         goods.number = number
#         goods.production = production
#         goods.safe_date = safe_date
#         goods.description = description
#         goods.picture = picture
#         goods.statue = 0
#         goods.save()
#         return HttpResponseRedirect('/PShop/list_goods/')
#     return render(request, 'pshop/list_goods.html', {'user': user})


@login_valid
def list_goods(request):
    goods_list = Goods.objects.all()
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)

    return render(request, 'pshop/list_goods.html', locals())


def set_goods(request, id):
    set_type = request.GET.get('set_type')
    goods = Goods.objects.get(id=int(id))
    if set_type == 'up':
        goods.statue = 1
    elif set_type == 'down':
        goods.statue = 0
    goods.save()
    return HttpResponseRedirect('/PShop/list_goods/')


@login_valid
def goods(request, id):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    goods_data = Goods.objects.get(id=int(id))
    return render(request, 'pshop/goods.html', locals())


@login_valid
def change_goods(request, id):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    if int(id) != 0:
        goods_data = Goods.objects.get(id=int(id))
        goods = Goods.objects.get(id=int(id))
    if request.method == 'POST':
        get_data = request.POST
        name = get_data.get('name')
        price = get_data.get('price')
        number = get_data.get('number')
        production = get_data.get('production')
        safe_date = get_data.get('safe_date')
        description = get_data.get('description')
        picture = request.FILES.get('picture')
        if int(id) == 0:
            global goods
            goods = Goods()
        goods.name = name
        goods.price = price
        goods.number = number
        goods.production = production.replace('年', '-').replace('月', '-').replace('日', '')
        goods.safe_date = safe_date
        goods.description = description
        if picture:
            goods.picture = picture
        goods.statue = 0
        goods.save()
        if int(id):
            return HttpResponseRedirect('/PShop/goods/%s' % id)
        else:
            return HttpResponseRedirect('/PShop/list_goods/')

    return render(request, 'pshop/change_goods.html', locals())


from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from DjangoPet.settings import PAZE_SIZE


class GoodsView(View):
    def get(self, request):
        result = {
            'version': 'v1',
            'code': '200',
            'data': [],
            'page_range': []
        }
        id = request.GET.get('id')
        if id:
            goods_data = Goods.objects.get(id=int(id))
            result['data'].append(
                {
                    'name': goods_data.name,
                    'price': goods_data.price,
                    'number': goods_data.number,
                    'production': goods_data.production,
                    'safe_date': goods_data.safe_date,
                    'picture': goods_data.picture,
                    'description': goods_data.description,
                    'statue': goods_data.statue
                }
            )
        else:
            page_number = request.GET.get('page', 1)
            keywords = request.GET.get('keywords')
            all_goods = Goods.objects.all()
            if keywords:
                all_goods = Goods.objects.filter(name__contains=keywords)
                result['referer'] = '&keywords=%s' % keywords
            paginator = Paginator(all_goods, PAZE_SIZE)
            page_data = paginator.page(page_number)
            result['page_range'] = list(paginator.page_range)
            goods_data = [{'id': g.id,
                           'name': g.name,
                           'price': g.price,
                           'number': g.number,
                           'production': g.production,
                           'safe_date': g.safe_date,
                           'picture': g.picture.url,
                           'description': g.description,
                           'statue': g.statue} for g in page_data
                          ]
            result['data'] = goods_data
        return JsonResponse(result)


def vue_list_goods(request):
    user_email = request.COOKIES.get('email')
    user = User.objects.get(email=user_email)
    return render(request, 'pshop/vue_list_goods.html', locals())

# Create your views here.
