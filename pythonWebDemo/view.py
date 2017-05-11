# _*_ coding:utf-8 _*_

from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
