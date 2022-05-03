from django.db import models
from datetime import datetime


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        db_table="t_department"


class AllUsers(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64, )
    age = models.IntegerField(verbose_name="年龄")
    phone = models.CharField(verbose_name="手机号", max_length=16, default="000")
    create_time = models.DateField(verbose_name="入职时间")

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 1.有约束
    #   - to，与那张表关联
    #   - to_field，表中的那一列关联
    # 2.django自动
    #   - 写的depart
    #   - 生成数据列 depart_id
    # 3.部门表被删除
    # ### 3.1 级联删除
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    # ### 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # 在django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    class Meta:
        db_table="t_allusers"


'''
# 用户表
class Users(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    signup_time = models.DateTimeField(default=datetime.now) # auto_now=True：保存时自动设置该字段为现在日期，最后修改日期

    def __str__(self):
        return self.name+":"+self.phone

    # 自定义对应的表名，默认表名：myapp_users
    class Meta:
        db_table="t_users"


# 学生表
class Stu(models.Model):
    # 自定义Stu表对应的Model类
    # 继承自models.Model，封装好了增删改查的操作

    #定义属性：默认主键自增id字段可不写
    id = models.AutoField(primary_key=True) # 主键
    name = models.CharField(max_length=16)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length=1)
    classid = models.CharField(max_length=8)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%d:%s:%s"%(self.id,self.name,self.age,self.sex,self.classid)

    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="t_stu"
'''


