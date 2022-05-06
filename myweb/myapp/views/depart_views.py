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


# 部门列表 
def departIndex(request):
    data_list = Department.objects.all()
    context = {"queryset": data_list}
    return render(request, "depart_list.html", context)

def depart_model_form_add(request):
    if request.method == "GET":
        form = DepartModelForm()
        return render(request, "depart_model_form_add.html", {"form": form})
    
    # POST提交表单
    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("departindex"))
    
    # 否则form可以自动携带错误信息
    return render(request, "depart_model_form_add.html", {"form": form})
    

def depart_model_form_edit(request, did):
    ob = Department.objects.get(id=did)
    if request.method == "GET":
        form = DepartModelForm(instance=ob)
        return render(request, "depart_model_form_edit.html", {"form": form})
    
    # POST提交修改:
    # 这里如果不加instance=ob，form.save()会默认在DB中新建一行数据
    form = DepartModelForm(data=request.POST, instance=ob)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("departindex"))
    
    return render(request, "depart_model_form_edit.html", {"form": form})

def del_depart(request, did):  
    try:
        Department.objects.get(id=did).delete()
        return HttpResponseRedirect(reverse("departindex"))
    except:
        return render(request, "info.html", {"reason": "删除部门失败", "from": "depart"})