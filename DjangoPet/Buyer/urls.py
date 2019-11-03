from django.urls import path, re_path
from Buyer.views import *


urlpatterns = [
    re_path(r'^$', index),
    path('index/', index),
    path('list/', list),
    re_path(r'goods/(?P<id>\d+)/', goods),
    path('cart/', cart),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('valid_email/', valid_email),
    # path('search_goods/', search_goods),
]