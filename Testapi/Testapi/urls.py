"""Testapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from apiMang import views
from django.conf.urls import  url
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^api_manage/$', views.api_manage),
    url(r'^accounts/login/$', views.index),
    url(r'^search_name/$', views.search_name),
    url(r'^project_manage/$', views.project_manage),
    url(r'^report_manage/$', views.report_manage),
    url(r'^logout/$', views.logout),
    url(r'^api/', include('apiMang.urls', namespace="apiMang")),
]
