from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from PShop.models import *
from PShop.views import set_password, valid_user


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
                if referer in ('http://127.0.0.1:8000/Buyer/login/',"None"):
                    referer = HttpResponseRedirect('/')
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
    response = HttpResponseRedirect('/')
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


def add_goods(request):
    goods = request.POST.get
