from django.contrib import admin
from django.urls import include, path
from app_intro.views import print_reqs
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('print_get_post_meta/', print_reqs, name='print_get_post_meta'),
    path('admin/', admin.site.urls),
]

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