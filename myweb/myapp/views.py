from re import M
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Stu, Users
from django.urls import reverse
from django.views import View
from datetime import datetime
# Create your views here.

'''
实战
'''

# 浏览用户信息        
def indexUsers(request):
    # 执行数据查询，并放置到模板中
    list = Users.objects.all()
    context = {"stulist":list}
    return render(request, "index.html", context)

# 加载添加信息表单
def addUsers(request):  
    return render(request,"add.html")

# 添加操作
def insertUsers(request): 
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,"info.html",context)

# 删除操作    
def delUsers(request,uid):  
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"info.html",context)

# 加载信息编辑表单    
def editUsers(request, uid):  
    try:
        ob = Users.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"info.html",context)

# 执行信息编辑操作
# 这个接口用于接收前端发来的POST请求，根据请求里的字段对数据库进行修改
def updateUsers(request):
    try:
        ob = Users.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.addtime = datetime.now
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"info.html",context)






'''
练习
'''
def tpl(request):
    context = {
        "name": "贾雨宁",
    }
    return render(request, 'tpl.html', context)

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