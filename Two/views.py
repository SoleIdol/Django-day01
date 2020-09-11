from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def foods(request):
    return render(request, 'foods.html')


def hello(request):
    return HttpResponse('hahahahhah')
