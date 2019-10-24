from django.shortcuts import render
from django.http import HttpResponseRedirect

from Pet.models import *





def index(request):
    goods_list = Goods.objects.all()
    return render(request, "pet/index.html", locals())


def about(request):
    return render(request, "pet/about.html", locals())


def pro(request):
    return render(request, "pet/pro.html", locals())
# Create your views here.
