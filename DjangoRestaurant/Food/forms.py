from django import forms


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=12,
        min_length=6,
        label='用户名'
    )
    password = forms.CharField(
        max_length=12,
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'title'}),
        required=True,
        label='密码',
        error_messages={'required': '密码不可以为空'}
    )

from Food.models import Foods
from django.forms import ModelForm


class FoodsForm(ModelForm):
    class Meta:
        model = Foods
        # fields = '__all__'
        fields = ('name', 'price', 'picture', 'description')
        labels = {
            'name':'食品名称',
            'price': '食品价格',
            'picture': '食品图片',
            'description': '食品描述',
        }