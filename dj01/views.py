from django.http import HttpResponse


def index(request):
    return HttpResponse('你好呀，恭喜第一次测试成功')


def hello(request):
    return HttpResponse('Hello , 我想死你了')
