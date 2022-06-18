from django.shortcuts import render

# Create your views here.
"""
视图 （Python函数）
视图函数两个要求
1、视图的第一个参数就是接受请求 这个请求就是HttpRequest的类对象
2、必须返回一个响应
"""

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    context = {
        'name': '618有惊喜'
    }

    return render(request,'book/index.html',context=context)