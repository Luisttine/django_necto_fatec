from django.contrib import admin
from django.urls import include, path

from app_intro.views import print_reqs, index
from app_intro import views


urlpatterns = [
    path('index/', include('app_intro.urls')), 


]

