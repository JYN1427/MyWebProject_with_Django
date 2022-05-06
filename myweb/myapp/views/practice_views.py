from curses.ascii import US
from dataclasses import field
from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import AllUsers, Department
from django.urls import reverse
from django.views import View
from datetime import datetime

from myapp.utils.form import UserModelForm, DepartModelForm
from myapp.utils.jyntools import jynTools as jyn

def tpl(request):
    context = {
        "names": ["贾雨宁", "沈卓瑶", "baby"],
        "mydict": {
            "1": "one", 
            "2": "two",
        },
    }
    return render(request, 'tpl.html', context)

def news(request):
    import requests as r
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
    url = 'http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/04/news'

    response = r.get(url=url, headers=headers)
    context = {
        "names": ["贾雨宁", "沈卓瑶", "baby"],
        "mydict": {
            "1": "one", 
            "2": "two",
        },

        # josn反序列化
        # 一个list，里面每条新闻都是一个dict
        "datas": response.json()
    }
    return render(request, 'tpl.html', context)

def somthing(request):
    # request是一个对象，封装了用户请求的所有相关数据

    # 1. 获取方法
    print(request.method)

    # 2. 获取URL上的数据
    print(request.GET)

    # 3. 获取请求体里的数据
    print(request.POST)

    '''
    return HttpResponseRedirect("https://www.baidu.com")
    return redirect("https://www.baidu.com")

    区别：
        HttpResponseRedirect仅可以接收url作为参数传入。
        Redirect可以接收model、view或者url作为参数传入，并返回HttpResponseRedirect。
    '''
    return redirect("https://www.baidu.com")


'''
# 练习

def index(request):
    # 重定向到name为find3的url，revers()反射
    return HttpResponseRedirect(reverse("find3", args=(100, "Sam Smith")))


def index1(request):
    try:
        mod = Stu.objects
        s = mod.get(name='jyn')
        return HttpResponse(s)
    except:
        return HttpResponse("没有找到对应的信息！")


def index2(request):
    return HttpResponse("szy你好！")

def view_DB(request):
    mod = Stu.objects
    slist = mod.all()
    res = []
    for s in slist:
        res.append(s)

    res.append(mod.get(id=1))
    return HttpResponse(res)

def find(request, sid = None, name = None):
    res = ""
    if sid: res += str(sid) + ", "
    if name: res += name
    return HttpResponse(res)

def date_data(request, year, month):
    return HttpResponse('参数信息：%s年%s月' % (year, month))
'''