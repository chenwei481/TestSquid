#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.conf.urls import url
from apiMang import views_if

urlpatterns = [
    # guest system interface:
    # ex : /api/add_event/
    url(r'^add_event/', views_if.add_case, name='add_case'),
]
