from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_request(self,request):

        print('11111111每次请求前,都会调用执行')

        username = request.COOKIES.get('name')
        if username is None:
            print('没有用户信息')
        else:
            print("有用户信息")

    def process_response(self,request,response):

        print('每次响应前,都会调用执行111111111')

        return response

class TestMiddleWare2(MiddlewareMixin):

    def process_request(self,request):

        print('2222222每次请求前,都会调用执行')
        #
        # username = request.COOKIES.get('name')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print("有用户信息")

    def process_response(self,request,response):

        print('每次响应前,都会调用执行22222222')

        return response