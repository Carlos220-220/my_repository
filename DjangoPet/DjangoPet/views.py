from django.shortcuts import render

def index(request):
    return render(request, "index.html", locals())

def about(request):
    return render(request, "about.html", locals())

def pro(request):
    return render(request, "pro.html", locals())