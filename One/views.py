from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def one1(request):
    return HttpResponse('这是One中的第一个视图函数')


def one2(request):
    return HttpResponse('<h1>灰原哀真可耐</h1>')
