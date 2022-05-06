from django import forms
from myapp.models import AllUsers, Department, PrettyNum

# 这里定义一个ModelForm类，用来描述该模型往前端传的：
#   1. 哪些字段
#   2. 各个字段的样式


# fields的写法:
# fields = ['name', 'password', 'age']
# fields = "__all__"
# exclude = ['level] # ModelForm里除了level字段都包括


'''用户表的ModelForm'''
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


'''部门表的ModelForm'''
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


# 验证器和验证器错误
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
'''号码表的ModelForm'''
class PrettyNumModelForm(forms.ModelForm):
    # 手机号的格式需要被约束
    '''
    # 验证方法1：写一个对该字段的约束，包含validators。
    mobile = forms.CharField(
        label="手机号", 
        validators=[RegexValidator(r'^1[3-9]{1}\d{9}$')], # 正则
    )
    '''

    class Meta:
        model = PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.label,
                }


    # 验证方法2：写一个钩子方法 def clean_字段名(self) 
    def clean_mobile(self):
        # self.cleaned_data是一个字典，存储了给当前ModelForm各个字段的赋值情况
        txt_mobile = self.cleaned_data["mobile"] # 取出来这次填写的mobile

        # 做格式、重复的校验
        if len(txt_mobile) != 11:
            raise ValidationError("手机号格式错误")
        elif PrettyNum.objects.filter(mobile=txt_mobile).exists():
            # 如果在编辑的时候也不希望重复：
            # PrettyNum.objects.filter(mobile=txt_mobile).exclude(id=self.instance.pk).exists():
            raise ValidationError("该手机号已经存在")
        return txt_mobile



# 编辑的时候可以禁止修改手机号, 用disabled=True
class PrettyNumModelFormWhenEdit(forms.ModelForm):
    # 手机号的格式需要被约束
    # 验证方法1：写一个对该字段的约束，包含validators。
    mobile = forms.CharField(
        label="手机号", 
        disabled=True
    )

    class Meta:
        model = PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.label,
                }