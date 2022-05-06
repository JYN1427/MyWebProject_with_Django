from curses.ascii import HT, US
from dataclasses import field
from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import PrettyNum
from django.urls import reverse
from django.views import View
from datetime import datetime

from myapp.utils.form import PrettyNumModelForm, PrettyNumModelFormWhenEdit
from myapp.utils.jyntools import jynTools as jyn
from myapp.utils.pagination import Pagination


page_size = 10

# 浏览号码信息
def pretty_index(request):
    # for i in range(100, 199):
    #     PrettyNum.objects.create(mobile="15000000"+str(i), price=i, level=1, status=1)

    # 创建filter取解析的关键字参数字典
    data_dict = {} 

    # 获取GET请求的参数
    query_dict = request.GET
    mobile_query = query_dict.get("mobile_query", "") # 前端传过来的搜索关键字, 如果没有就赋空字符串""
    
    if mobile_query:
        # 包含式搜索
        data_dict["mobile__contains"] = mobile_query

    # 查找, 并按照level进行desc排序（高级别在前的展示方式）, 分页
    queryset = PrettyNum.objects.all().filter(**data_dict).order_by("-level")

    # 分页组件对象
    page_object = Pagination(request, queryset)
    context = {
        # 1.搜索的东西，方便输入框保持
        'search_data': mobile_query,
        
        # 2.分页字段：
        # 'queryset': queryset,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 页码的一系列html语句
        'now_page': page_object.page,
    }

    return render(request, "pretty_list.html", context)


# 添加号码
def pretty_model_form_add(request):
    if request.method == "GET":
        form = PrettyNumModelForm()
        return render(request, "pretty_model_form_add.html", {'form': form})
    
    form = PrettyNumModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("prettyindex"))
    
    return render(request, "pretty_model_form_add.html", {'form': form})


# 编辑号码
def pretty_model_form_edit(request, pid):
    ob = PrettyNum.objects.get(id=pid)
    if request.method == "GET":
        form = PrettyNumModelFormWhenEdit(instance=ob)
        return render(request, "pretty_model_form_edit.html", {'form': form})
    
    form = PrettyNumModelFormWhenEdit(data=request.POST, instance=ob)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("prettyindex"))
    
    return render(request, "pretty_model_form_edit.html", {'form': form})


# 删除号码
def del_pretty(request, pid):
    try:
        ob = PrettyNum.objects.get(id=pid).delete()
        return HttpResponseRedirect(reverse("prettyindex"))
    except:
        return render(request, "info.html", {"reason": "删除号码失败", "from": "pretty"})


# 搜索 笔记
def search(request):
    data_dict = {
        "mobile": "13051393587",
        "level": 1,
    }
    PrettyNum.objects.filter(**data_dict)

    # 数字范围筛选
    PrettyNum.objects.filter(id=3) # 等于
    PrettyNum.objects.filter(id__gt=3) # 大于
    PrettyNum.objects.filter(id__gte=3) # 大于等于
    PrettyNum.objects.filter(id__lt=3) # 小于
    PrettyNum.objects.filter(id__lte=3) # 小于等于

    # 字符串筛选
    data_dict = {"mobile__contains": "130"}
    PrettyNum.objects.filter(**data_dict)

    PrettyNum.objects.filter(mobile="13051393587")
    PrettyNum.objects.filter(mobile__startwith="130")
    PrettyNum.objects.filter(mobile__endwith="130")
    PrettyNum.objects.filter(mobile__contains="130")

# 分页 笔记
def page(request):
    PrettyNum.objects.all()[0:10]
    PrettyNum.objects.filter(mobile__contains="130")[10:20]