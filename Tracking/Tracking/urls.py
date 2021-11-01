"""Tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GPS import views


urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    
    path('',views.home,name="home"),
    path('add_device/',views.add_device,name="add_device"),
    path('update_device/<str:pk>/',views.update_device,name="update_device"),
    path('delete_device/<str:pk>/',views.delete_device,name="delete_device"),
    path('device/<str:pk>/',views.device,name="device"),
    path('track/<str:pk>/',views.track,name="track"),
    path('user/',views.userPage,name="userPage"),
    path('user_from_admin/<str:pk>/',views.user_from_admin,name="user_from_admin"),
    path('delete_user/<str:pk>/',views.delete_user,name="delete_user"),

    
    

    
    
    
    

    
]
