"""DjangoRestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from DjangoRestaurant.views import *
from Food.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('shop/', shop),
    path('find_shop/', find_shop),
    path('shop-con/', shop_con),
    # re_path(r'shop-con/(?P<id>[1-9]+)/', shop_con),
    path('ap/', ajax_post),
    path('agd/', ajax_g_data),
    path('check/', check),
    path('form_check/', form_check),
    path('p_form/', p_form),
    re_path(r'news/(?P<page>\d+)/', news),
    path('setCookie/', setCookie),
    path('del_cookie/', del_cookie),
    path('register/', register),
    # path('login/', login),
    path('logout/', logout),
    path('shop_login/', shop_login),
    # path('foods/', csrf_exempt(FoodView.as_view())),
    path('meishi/', meishi),
]

from Food.urls import router

urlpatterns += router.urls


urlpatterns += [
    # path('add_foods_type/', add_foods_type),
    # path('add_foods/', add_foods),
    # path('add_news/', add_news),
    # path('add_shop/', add_shop),
    # path('add_company/', add_company),
    # path('request_r/', request_r),
    # path('find_food/', find_food)
]

urlpatterns += [
    path('foods/', csrf_exempt(FoodView.as_view())),
]