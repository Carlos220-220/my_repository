from django.urls import path, re_path
from PShop.views import *


urlpatterns = [
    re_path(r'^$', index),
    path('index/', index),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('forget_password/', forget_password),
    path('reset_password/', reset_password),
    path('change_password/', change_password),
    path('profile/', profile),
    path('set_profile/', set_profile),
    path('profile_password/', profile_password),
    path('list_goods/', list_goods),
    re_path(r'^set_goods/(?P<id>\d+)/', set_goods),
    re_path(r'^goods/(?P<id>\d+)/', goods),
    re_path(r'change_goods/(?P<id>\d+)/', change_goods),
    path('Goods/', GoodsView.as_view()),
    path('vue_list_goods/', vue_list_goods),
    path('order_list/', order_list),
    path('send_shop/', send_shop),
]