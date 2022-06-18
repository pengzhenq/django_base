
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from book.models import BookInfo,PeopleInfo
import json

# Create your views here.



def index(request):

    # book=BookInfo.objects.create(
    #     name = 'abc',
    #     pub_date = '2020-1-1',
    #     readcount = 10
    # )

    return HttpResponse('index')

def shop(request,city_id,mobile):

    query_params = request.GET
    # print(query_params)
    # # print(query_params.get('order'))
    # print(query_params['order'])

    #<QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>
    #QueryDict具体字典特性，还有一键多值
    # print(query_params.get('order'))

    print(city_id,mobile)

    print(query_params.getlist('order'))
    return HttpResponse('shop')

def register(request):

    data = request.POST
    print(data)

    return HttpResponse('ok')

def json_test(request):

    # json_data = request.body
    #
    # json_str=json_data.decode()
    #
    # json_dict = json.loads(json_data.decode())
    # print(json_dict)

    ##################请求头数据#######################
    request_header = request.META['SERVER_PORT']
    print(request_header)
    return HttpResponse('json')


def method(request):

    print(request.method)

    print(request.user)

    return HttpResponse('method')

def res(request):

    # response = HttpResponse('res')
    #
    # response['name'] = 'itcast'

    # data = {
    #     'name': 'itcast',
    #     'address': 'changsha'
    # }

    data_dict = [
        {
            'name': 'liuyifeng',
            'address': 'sb'
        },
        {
            'name': 'zengkun',
            'address': 'nc'
        }
    ]

    #json.dumps 将字典转换成JSON字符串
    #json.loads 将JSON字符串转换成字典

    data = json.dumps(data_dict)

    # response = JsonResponse(data,safe=False)
    response = HttpResponse(data)

    return response

def redirect_test(request):

    return redirect('https://www.baidu.com')

def set_cookies(request):

    # 获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 服务器设置cookie信息
    response = HttpResponse('set_cookies')

    # 通过响应对象.set_cookie方法
    # key value
    response.set_cookie('name',username,max_age=60*60)
    # return HttpResponse('set_cookies')

    response.set_cookie('pwd',password)

    # response.delete_cookie('pwd')
    #
    return response

def get_cookies(request):

    data = request.COOKIES.get('name')

    return HttpResponse(data)


###############################################################
# session是保存在服务器端的并且依赖于cookie

"""
第一次请求 ，会在服务器端设置session信息
服务器同时生成一个session的cookie信息
浏览器接受这个信息之后，会把cookie信息保存   ---------依赖于cookie


第二次及其之后的请求，都会携带这个sessionid，服务器会验证这个sessionid，验证没有问题会读取相关数据，实现业务逻辑

"""

def set_session(request):

    username = request.GET.get('username')
    user_id = 1

    request.session['user_id'] = user_id
    request.session['username'] = username


    return HttpResponse('set_session')

def get_session(request):

    user_id = request.session.get('user_id')
    username = request.session.get('username')


    content = '{},{}'.format(user_id,username)

    return HttpResponse(content)


############################类视图#############################

def login(request):

    if request.method == "GET":
        return HttpResponse('GET逻辑')
    elif request.method == "POST":
        return HttpResponse('POST逻辑')


"""
类视图的定义

class 类视图名字（View):
    
    def get(self,request):
    
        return HttpResponse('get,get,get')
    
    def http_method_lower(self,request):
    
        return HttpResponse('post,post,post')

1、继承自View

"""

from django.views import View


class LoginView(View):

    def get(self,request):

        return HttpResponse('get,get,get')

    def post(self,request):

        return HttpResponse('post,post,post')


##############################
"""
我的订单、个人中心页面
如果登录用户 可以访问

如果未登录用户，不应该访问，应该跳转到登录页面

定义一个订单、个人中心 类视图

如何定义有没有登录，使用admin站点管理为例
"""

#LoginRequiredMixin 作用，只有登录用户才可以访问页面
from django.contrib.auth.mixins import LoginRequiredMixin

class OrderLogin(LoginRequiredMixin,View):

    def get(self,request):

        return HttpResponse('个人中心')

    def post(self,request):

        return HttpResponse('post')
