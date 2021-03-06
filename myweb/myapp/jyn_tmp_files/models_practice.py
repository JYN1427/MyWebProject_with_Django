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


