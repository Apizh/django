from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def method(request):
    return HttpResponse("<html><h1>Hello, world. You're at the polls index.</h1></html>")


def method1(request):
    return HttpResponse("<h1>Hello, world. This second page</h1>")