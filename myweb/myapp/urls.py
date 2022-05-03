# 自己创建的app的子路由文件, re_path表示用正则匹配
from django.urls import path, re_path
from myapp import views

# 命名
urlpatterns = [
    
    # 用户信息管理系统：
    path('users/', views.usersIndex, name="usersindex"), #浏览用户信息
    path('users/add/', views.addUsers, name="addusers"), #加载添加用户信息表单
    path('users/insert/', views.insertUsers, name="insertusers"), #执行用户信息添加
    path('users/<int:uid>/del/', views.delUsers, name="delusers"), #执行用户信息删除
    path('users/<int:uid>/edit/', views.editUsers, name="editusers"), #加载用户信息编辑表单
    path('users/update', views.updateUsers, name="updateusers"), #执行用户信息编辑
    # 用户登录
    path('login/', views.login, name="login"), 
    # 错误提示
    path('info/', views.info, name="info"), 
    
    # 简单练习
    path('tpl/', views.tpl, name="tpl"),
    # 通过requests做接口请求去获取联通的新闻
    path('news/', views.news, name="news"), 
    # 获取请求的方法、数据。重定向的两种方式。
    path('somthing/', views.somthing, name="somthing"), 

    

    # ModelForm
    # 添加用户
    path('users/modelform/add', views.user_model_form_add, name="addusers_by_ModelForm"),
    path('users/modelform/edit/<int:uid>', views.user_model_form_edit, name="editusers_by_ModelForm"), 


    # 用户信息管理系统：
    path('depart/', views.departIndex, name="departindex"), #浏览部门信息
    path('depart/del/<int:did>', views.deldepart, name="deldepart"), #执行部门信息删除
    path('depart/modelform/add', views.depart_model_form_add, name="adddepart_by_ModelForm"), # 添加部门
    path('depart/modelform/edit/<int:did>', views.depart_model_form_edit, name="editdepart_by_ModelForm"),  # 编辑部门


    
]


'''
    path('', views.index, name = 'index'),
    path('jyn/', views.index1, name = 'index1'),
    path('szy/', views.index2, name = 'index2'),
    path('db/', views.view_DB, name = 'view_DB'),
    path('find/', views.find, name = 'find1'),
    path('find/<int:sid>/', views.find, name = 'find2'),
    path('find/<int:sid>/<str:name>/', views.find, name = 'find3'),
    re_path(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.date_data, name = 'date'),
'''