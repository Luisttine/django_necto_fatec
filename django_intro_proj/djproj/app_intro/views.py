from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def print_reqs(request):
    print (request)
    return HttpResponse('hello world')

@csrf_exempt
def print_reqs(request):
    print ("\n-------META--------------\n")
    print(request.META)
    print ("\n-------REQUEST--------------\n")
    print (request)
    print ("\n-------REQUEST POST--------------\n")
    print (request.POST)
    print ("\n-------REQUEST GET--------------\n")
    print (request.GET)
    return HttpResponse('olá mundo')

def index(request):
    template_name = 'app_intro/teste.html'

    return render('resquest', template_name, content_type='application/xhtml+xml')