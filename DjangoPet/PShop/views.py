from django.shortcuts import render
from django.http import HttpResponseRedirect
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
                return error
        else:
            error = '用户名不存在!'
            return error
    return render(request, 'pshop/login.html', locals())


@login_valid
def index(request):
    return render(request, 'pshop/index.html')


# 退出登陆
def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('email')
    response.delete_cookie('user_id')
    request.session.clear()
    return response


def forget_password(request):
    return render(request, 'pshop/forgot-password.html')
# Create your views here.
