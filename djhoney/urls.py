from django.contrib import admin
from django.urls import path, re_path

from apps.user import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # user模块
    re_path('login', views.LoginView.as_view(), name='login'),
    re_path('register', views.RegisterView.as_view(), name='register'),
]
