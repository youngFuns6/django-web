# -*- coding = utf-8 -*-
# @Author: youngFuns
# Time : 2021/12/15 5:23 PM
# @File : urls
# Product : django_web

from django.urls import path
from goods.views import goodslist

urlpatterns = [
    path('goodslist/', goodslist)
]
