from django.shortcuts import render_to_response, render
from News.models import *
from django.http import HttpResponse
from django.db.models import Max, Min, Count, Sum, Avg, F, Q



def ajax_get(request):
    return render_to_response('ajax_get.html', locals())

from django.http import JsonResponse
def find_news(request):

    # #获取所有的标题新闻
    # data_list = [{'title': titles.title}for titles in News.objects.all()]

    #模糊查询新闻标题
    get_news = request.GET.get('get_title')
    data_list = []
    if get_news:
        news_list = News.objects.filter(title__contains=get_news)
        for n in news_list:
            data_list.append({'title': n.title})

    return  JsonResponse({'data_list': data_list})



def form_get(request):
    news_list = News.objects.all()
    data1 = request.GET.get('name')
    data2 = request.GET.get('title')
    data3 = request.GET.get('pwd')
    get_data1 = []
    if data1:
        get_data1 = News.objects.filter(title__contains=data1)

    return render_to_response('form_get.html', locals())

def form_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        title = request.POST.get('title')
        title_list = []
        if title:
            title_list = News.objects.filter(title__contains=title)

    return render(request, 'form_post.html', locals())

def add_editor(request):
    editors = Editor()
    editors.name = '市丸银'
    editors.email = 'swy@qq.com'
    editors.save()
    return HttpResponse('保存成功')


def add_News(request):
    for i in range(5):
        news = News()
        news.title = '新闻标题%d' % i
        news.time = '1999-09-09'
        news.description = '新闻描述'
        news.image = '1.jpg'
        news.content = '新闻内容%d' % i
        news.type_id = NewsType.objects.get(id=1)
        # news.save()
    return HttpResponse('保存成功')


def add_type(request):
    news_type = NewsType()
    news_type.label = '诗歌'
    news_type.description = '大师唱的歌'
    # news_type.save()
    return HttpResponse('保存成功')


def index(request):
    news_list = News.objects.all()
    return render_to_response('index.html', locals())


def news_con(request, id):
    news = News.objects.get(id=int(id))
    return render_to_response('news-con.html', locals())


def selectExample(request):
    # news = News.objects.get(id=4).delete()
    news_list = News.objects.all()
    editor_list = Editor.objects.all()

    editor1 = News.objects.get(id=1).editor_id.all()
    editor2 = Editor.objects.get(id=1).news_set.all()
    # editor_news_list = News.objects.get(id=1).editor_id.all()

    # news = News.objects.raw('select * from auth_user')
    # method = dir(news)
    news = News.objects.values('title').all()
    return render_to_response('select.html', locals())

def vueExample(request):
    return render_to_response('vueExample.html', locals())

