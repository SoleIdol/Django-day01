from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('主页面')


def test(request):
    return render(request, 'test.html')


