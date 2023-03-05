from django.contrib import admin
from django.urls import path, re_path

from apps.user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', views.index),
    re_path('register', views.register, name='register'),
]
