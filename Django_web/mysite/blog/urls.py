# -*- coding:utf-8 -*-
from django.urls import path
from . import views

# 将url传入view.index模块中， index类别名name
urlpatterns = [path(r'', views.index, name='index'), ]
