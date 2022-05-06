from curses.ascii import HT, US
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



# 浏览用户信息        
def usersIndex(request):
    # 搞一个如果是get，就去info.htl 请先登录 

    # 执行数据查询，并放置到模板中
    data_list = AllUsers.objects.all()
    context = {"queryset": data_list}
    return render(request, "user_list.html", context)

# 加载添加信息表单
def addUsers(request):  
    context = {
        'gender_choices': AllUsers.gender_choices,
        'depart_list': Department.objects.all(),
    }
    return render(request,"user_add.html", context)

# 添加操作
def insertUsers(request): 
    try:
        '''
        # 方法1
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.save()
        '''
        # 方法2
        # 获取用户提交的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        ctime = request.POST.get('ctime')
        gender = request.POST.get('gd')
        depart_id = request.POST.get('dp')


        # 添加到数据库中
        AllUsers.objects.create(name=user, password=pwd, age=age,
                                        phone=phone, create_time=ctime,
                                        gender=gender, depart_id=depart_id)
        
        jyn.MyINFO(str(user)+"添加成功")
        return HttpResponseRedirect(reverse("usersindex"))

    except:
        return render(request,"info.html", {"reason": "添加用户失败", "from": "user"})

# 删除操作    
def delUsers(request,uid):  
    try:
        AllUsers.objects.get(id=uid).delete()
        # 或者：Users.objects.filter(id=uid).delete()
        # 如果只想取第一条数据：Users.objects.filter(id=uid).first()
        # 如果想数据全删除：Users.objects.all().delete()
        return HttpResponseRedirect(reverse("usersindex"))
    except:
        context = {'reason':'删除用户失败！', "from": "user"}
        return render(request, "info.html",context)

# 加载信息编辑表单    
def editUsers(request, uid):  
    try:
        ob = AllUsers.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"user_edit.html",context)
    except:
        context = {'reason':'没有找到要修改的信息！', "from": "user"}
        return render(request, "info.html",context)

# 执行信息编辑操作
# 这个接口用于接收前端发来的POST请求，根据请求里的字段对数据库进行修改
def updateUsers(request):
    try:
        ob = AllUsers.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        # ob.addtime = datetime.now
        ob.save()
        # 或者：
        # Users.objects.filter(id=request.POST['id']).update(name=request.POST['name'], age=request.POST['age'],phone = request.POST['phone'])
        return HttpResponseRedirect(reverse("usersindex"))
    except:
        context = {'reason':'修改失败！', "from": "user"}
        return render(request, "info.html",context)



################## ModelFo rm########################

def user_model_form_add(request):
    ''' 添加用户 '''
    if request.method == "GET":
        form = UserModelForm()
        context = {
            'form': form,
        }
        return render(request, 'user_model_form_add.html', context)
    
    # 用户提交了POST数据
    form = UserModelForm(data=request.POST)

    # 校验数据的合法性
    if form.is_valid():
        # print(form.cleaned_data)
        '''
        除了用户输入的值，还有别的字段也想更新，怎么做？
        form.instance.字段名 = 值
        '''
        form.save()
        return HttpResponseRedirect(reverse("usersindex"))
    
    # 如果不合法，在页面上提示错误
    context = {'form': form}
    # 此时的form是有data的，而且还包含了is_valid()之后的错误信息
    return render(request, 'user_model_form_add.html', context)


def user_model_form_edit(request, uid):
    ob = AllUsers.objects.get(id=uid)

    # 从user_list.html点击编辑，get方法进来：
    if request.method == "GET":
        # 指明instance之后，html里就不需要指明value字段了
        form = UserModelForm(instance=ob)
        context = {'form': form, }
        return render(request, "user_model_form_edit.html", context)
    
    # 提交编辑后的信息，post方法提交表单进来：
    # 这里如果不加instance=ob，form.save()会默认在DB中新建一行数据
    form = UserModelForm(data=request.POST, instance=ob)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("usersindex"))
    
    context = {'form': form, }
    return render(request, "user_model_form_edit.html", context)