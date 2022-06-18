from django.urls import path
from book.views import index, shop, register, json_test, method, res, redirect_test, set_cookies, get_cookies, \
    set_session, get_session, login, LoginView, OrderLogin
from django.urls import converters
from django.urls.converters import register_converter

#1、定义转换器
class Mobile_Converter:
    #匹配手机号码的正则
    #验证数据的关键是：正则
    regex = '1[3-9]\d{9}'

    #将匹配结果传递到视图内部使用
    #相当于对mobile数据进行一个验证和装饰
    def to_python(self, value):
        return value

    #将匹配结果用于反向解析传值时使用
    # def to_url(self, value):
    #     return value

#2、先注册转换器，才能在第三步中使用
#convert转换器类
#type_name 转换器的名字

# def register_converter(converter, type_name):
#     REGISTERED_CONVERTERS[type_name] = converter()
#     get_converters.cache_clear()


register_converter(Mobile_Converter,'phone')


urlpatterns = [
    path('index/',index),
    #<转换器名字：变量名>
    #转换器会对变量数据进行验证

    path('<int:city_id>/<phone:mobile>',shop),
    path('register/',register),
    path('json/',json_test),
    path('method/',method),
    path('res/',res),
    path('redirect/',redirect_test),
    path('set_cookies/',set_cookies),
    path('get_cookies/',get_cookies),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('login/',login),
    path('loginview/',LoginView.as_view()),
    path('orderlogin/',OrderLogin.as_view())
]