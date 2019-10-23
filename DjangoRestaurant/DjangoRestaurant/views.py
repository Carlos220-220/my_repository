from django.shortcuts import render_to_response
from Food.models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import hashlib
import json


from django.views import View

class FoodView(View):
    def __init__(self, **kwargs):
        super(FoodView,self).__init__()
        self.result = {
            'version':'v1.0',
            'code':200,
            'data':[

            ]
        }
    def get(self, request):
        id = request.GET.get('id')
        if id:
            try:
                data = Foods.objects.get(id=id)
            except Exception as e:
                self.result['code'] = 500
                self.result['data'].append(str(e))
            else:
                d = {'name':data.name,'price':data.price,'picture':data.picture.url,'description':data.description,'type':data.type_id.label}
                self.result['data'].append(d)
        else:
            data = [{'name':data.name,'price':data.price,'picture':data.picture.url,'description':data.description,'type':data.type_id.label} for data in Foods.objects.all()]
            self.result['data'] = data
        return JsonResponse(self.result)




    def post(self, request):
        return JsonResponse({'data':'这个是个post请求'})
    def put(self, request):
        return JsonResponse({'data':'这是个put请求'})
    def delete(self, request):
        return JsonResponse({'data':'这是个delete请求'})















# from django.views import View
#
# class FoodView(View):
#     def __init__(self, **kwargs):
#         super(FoodView, self).__init__()
#         self.result = {
#             "version": "v1.0",
#             "code": 200,
#             "data": []
#         }
#
#     def is_exit(self,id):
#         try:
#             data = Foods.objects.get(id=id)
#         except Exception as e:
#             self.result["code"] = 500
#             self.result["data"].append(str(e))
#             return False
#         else:
#             return data
#
#     def one_data(self,data):
#         d = {
#             "name": data.name,
#             "price": data.price,
#             "picture": data.picture.url,
#             "description": data.description,
#             "type": data.type_id.label
#         }
#         self.result["data"].append(d)
#
#
#     def get(self, request):
#         id = request.GET.get('id')
#         if id:
#             data = self.is_exit(id)
#             if data:
#                 self.one_data(data)
#
#         else:
#             data = [{
#                 "name": data.name,
#                 "price": data.price,
#                 "picture": data.picture.url,
#                 "description": data.description,
#                 "type": data.type_id.label
#             }for data in Foods.objects.all()]
#             self.result["data"] = data
#         return JsonResponse(self.result)
#
#     def post(self,request):
#         post_data = request.POST
#         name = post_data.get('name')
#         price = post_data.get('price')
#         picture = post_data.get('picture')
#         description = post_data.get('description')
#         type_id = post_data.get('type_id')
#
#         foods = Foods()
#         foods.name = name
#         foods.price = price
#         foods.picture = picture
#         foods.description = description
#         foods.type_id = FoodsType.objects.get(id=int(type_id))
#         foods.save()
#         self.one_data(foods)
#         return JsonResponse(self.result)
#
#
#     def put(self, request):
#         put_data = json.loads(request.body.decode())
#         id = put_data.get('id')
#         name = put_data.get('name')
#         price = put_data.get('price')
#         picture = put_data.get('picture')
#         description = put_data.get('description')
#         type_id = put_data.get('type_id')
#
#         foods = self.is_exit(id)
#         if foods:
#             foods.name = name
#             foods.price = price
#             foods.picture = picture
#             foods.description = description
#             foods.type_id = FoodsType.objects.get(id=int(type_id))
#             foods.save()
#             self.one_data(foods)
#
#         return JsonResponse(self.result)
#
#     def delete(self,request):
#         delete_data = json.load(request.body.decode())
#         id = delete_data.get('id')
#         foods = self.is_exit(id)
#         if foods:
#             d = {
#                 "name": foods.name,
#                 "price": foods.price,
#                 "picture": foods.picture.url,
#                 "description": foods.description,
#                 "type": foods.type_id.label
#             }
#             self.result["data"].append(d)
#             foods.delete()
#         return JsonResponse(self.result)
#









def loginValid(fun):
    def inner(request, *args, **kwargs):
        cookie_username = request.COOKIES.get('username')
        session_username = request.session.get('username')
        if cookie_username and session_username and cookie_username == session_username:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/shop_login/')
    return inner


def logout(request):
    response = HttpResponseRedirect('/shop_login/')
    response.delete_cookie('username')
    del request.session['username']
    return response

def shop_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            post_password = set_password(password)
            if post_password == user.password:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username', user.username)
                request.session['username'] = user.username
                return response
    return render(request, 'shop_login.html', locals())

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User()
        user.username = username
        user.password = set_password(password)
        user.save()
    return render(request, 'register.html', locals())


# def loginValid(fun):
#     def inner(request, *args, **kwargs):
#         cookie_username = request.COOKIES.get('username')
#         session_username = request.session.get('username')
#         if cookie_username and session_username and cookie_username == session_username:
#             return fun(request, *args, **kwargs)
#         else:
#             return HttpResponseRedirect('/login/')
#     return inner
#
@loginValid
def index(request):
    news_list = News.objects.order_by('-time')[0:8]
    return render(request, 'index.html', locals())

# def index(request):
#     cookie_username = request.COOKIES.get('username')
#     session_username = request.session.get('username')
#     if cookie_username and session_username and cookie_username == session_username:
#         news_list = News.objects.order_by('-time')[0:8]
#         return render(request, 'index.html', locals())
#     else:
#         return HttpResponseRedirect('/login/')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = User.objects.filter(username=username).first()
#         if user:
#             post_password = set_password(password)
#             if user.password == post_password:
#                 response = HttpResponseRedirect('/index/')
#                 response.set_cookie('username', user.username)
#                 request.session['username'] = user.username
#                 return response
#     return render(request, 'login.html', locals())
#
# def logout(request):
#     response = HttpResponseRedirect('/login/')
#     response.delete_cookie('username')
#     del request.session['username']
#     return response
#
# def set_password(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode())
#     result = md5.hexdigest()
#     return result
#
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = User()
#         user.username = username
#         user.password = set_password(password)
#         user.save()
#     return render(request, 'register.html', locals())





def setCookie(request):
    response = render(request, 'index.html')
    response.set_cookie('username', 'laobian')
    response.set_cookie('age', '18')
    return response

def del_cookie(request):
    response = render(request, 'index.html')
    response.delete_cookie('username')
    response.delete_cookie('age')
    return response




def shop(request):
    shop_list = Shop.objects.all()
    cookie_username = request.COOKIES.get('username')

    return render_to_response('shop.html', locals())


def find_shop(request):
    shop_name = request.GET.get('shop_name')
    shop_data = []
    if shop_name:
        shop_list = Shop.objects.filter(name__contains=shop_name)
        for s in shop_list:
            shop_data.append({'name': s.name, 'id': s.id, 'picture': s.picture.url, 'address': s.address})

    return JsonResponse({'shop_data': shop_data})


def shop_con(request, id):
    shop = Shop.objects.get(id=int(id))
    return render_to_response('shop-con.html', locals())


def ajax_post(request):
    return render(request, 'ajax_post.html', locals())


def ajax_g_data(request):
    result = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        result = '知道了,你是%s' % name
    return JsonResponse({'result': result})


def check(request):
    return render(request, 'check.html', locals())


def form_check(request):
    if request.method == 'POST':
        username = request.Post.get('username')
        password = request.POST.get('password')
        if username and password:
            pass
        else:
            error = '用户名密码不可以为空'
    return render(request, 'form_check.html', locals())


from Food.forms import *


def p_form(request):
    userform = UserForm()
    foodform = FoodsForm()
    return render(request, 'p_form.html', locals())


from django.core.paginator import Paginator



# @loginValid
def news(request, page):
    news_list = News.objects.order_by('-time')
    page_obj = Paginator(news_list, 5)
    page_data = page_obj.page(int(page))
    return render(request, 'news.html', locals())
