# 自己创建的app的子路由文件, re_path表示用正则匹配
from django.urls import path, re_path
from myapp import views

# 命名
urlpatterns = [
    path('', views.index, name = 'index'),
    path('jyn/', views.index1, name = 'index1'),
    path('szy/', views.index2, name = 'index2'),
    path('db/', views.view_DB, name = 'view_DB'),
    path('find/', views.find, name = 'find1'),
    path('find/<int:sid>/', views.find, name = 'find2'),
    path('find/<int:sid>/<str:name>', views.find, name = 'find3'),
    re_path(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.date_data, name = 'date'),

    # 用户信息管理系统：
    path('users', views.indexUsers, name="users"), #浏览用户信息
    path('users/add', views.addUsers, name="addusers"), #加载添加用户信息表单
    path('users/insert', views.insertUsers, name="insertusers"), #执行用户信息添加
    path('users/<int:uid>/del', views.delUsers, name="delusers"), #执行用户信息删除
    path('users/<int:uid>/edit', views.editUsers, name="editusers"), #加载用户信息编辑表单
    path('users/update', views.updateUsers, name="updateusers"), #执行用户信息编辑

    path('tpl', views.tpl, name="tpl"),

    
]