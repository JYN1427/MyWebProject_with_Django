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



def login(request):
    context = {
        "error_msg": "登录失败，用户名/密码错误",
    }
    
    # 从url进来的
    if request.method == "GET":
        # print(request.GET)
        # return render(request, "login.html")
        return render(request, "user_login.html")
        
    # 从提交form表单进来的(action)
    # elif request.method == "POST":
    # print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(username, password)
    if username=='root' and password == '1427':
        return HttpResponseRedirect(reverse("usersindex"))
    else:
        return render(request, "user_login.html", context)


def info(request):
    return render(request, "info.html")