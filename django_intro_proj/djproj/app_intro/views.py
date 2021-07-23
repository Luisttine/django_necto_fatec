from django.shortcuts import render
from django.http import HttpResponse

def print_reqs(request):
    print (request)
    return HttpResponse('hello world')