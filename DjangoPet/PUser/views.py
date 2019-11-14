from django.shortcuts import render
from PUser.models import *
import hashlib


# 设置密码
def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# 查重用户
def valid_user(email):
    try:
        db_email = User.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return db_email


# 添加用户
def add_user(**kwargs):
    if 'email' in kwargs and 'username' not in kwargs:
        kwargs['username'] = kwargs['email']
    user = User.objects.create(**kwargs)
    return user



# Create your views here.
