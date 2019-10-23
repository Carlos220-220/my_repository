"""DjangoTest URL Configuration

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
from django.urls import path,re_path
from DjangoTest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    re_path(r'news-con/(?P<id>\d+)/', news_con),
    path('add_type/', add_type),
    path('add_News/', add_News),
    path('add_editor/', add_editor),
    path('select/', selectExample),
    path('form_get/', form_get),
    path('form_post/', form_post),
    path('ajax_get/', ajax_get),
    path('find_news/', find_news),
    path('vueExample/', vueExample),
]
