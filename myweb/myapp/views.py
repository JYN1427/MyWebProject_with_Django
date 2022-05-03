from curses.ascii import US
from dataclasses import field
from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import AllUsers, Department
from django.urls import reverse
from django.views import View
from datetime import datetime

import logging
logger = logging.getLogger('django')
def MyINFO(s):
    t = "****"
    logger.info(t+s)

'''
实战
'''

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
        context = {'info':'添加成功！'}
        MyINFO(str(user)+"添加成功")

    except:
        context = {'info':'添加失败！'}

    return render(request,"info.html",context)

# 删除操作    
def delUsers(request,uid):  
    try:
        AllUsers.objects.get(id=uid).delete()
        # 或者：Users.objects.filter(id=uid).delete()
        # 如果只想取第一条数据：Users.objects.filter(id=uid).first()
        # 如果想数据全删除：Users.objects.all().delete()
        return HttpResponseRedirect(reverse("usersindex"))
    except:
        context = {'info':'删除失败！'}
    return render(request,"info.html",context)

# 加载信息编辑表单    
def editUsers(request, uid):  
    try:
        ob = AllUsers.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"user_edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"info.html",context)

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
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"info.html",context)


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


'''
武沛齐
'''
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


##########################################
from django import forms

# 这里定义一个ModelForm类，用来描述该模型往前端传的：
#   1. 哪些字段
#   2. 各个字段的样式
class UserModelForm(forms.ModelForm):
    class Meta:
        model = AllUsers
        fields = ['name', 'password', 'age', 'gender', 'phone', 'create_time', 'depart']
        '''
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'create_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
        '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(name, field)
            if name == "create_time":
                field.widget.attrs = {
                    'id': "start_id",
                    'type': "text",
                    'class': "form-control",
                    'placeholder': field.label,
                }
            else:
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': field.label,
                    }

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
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("usersindex"))
    else:
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
    form = UserModelForm(data=request.POST, instance=ob)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("usersindex"))
    
    context = {'form': form, }
    return render(request, "user_model_form_edit.html", context)



# 部门列表
class DepartModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.label,
                }

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
    return HttpResponseRedirect(reverse("departindex"))

def deldepart(request, did):  
    try:
        Department.objects.get(id=did).delete()
        return HttpResponseRedirect(reverse("departindex"))
    except:
        context = {'info':'删除失败！'}
    return HttpResponseRedirect(reverse("info"))