from django.contrib import admin
from django.urls import include, path
from app_intro.views import print_reqs, index

urlpatterns = [
    path('print_get_post_meta/', print_reqs, name='print_get_post_meta'),
    path('admin/', admin.site.urls),
    path('index', index)
]

