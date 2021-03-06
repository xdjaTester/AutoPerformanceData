#!/usr/bin/env python      
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
__author__ = 'zhouliwei'

"""
function:
date:2016/11/29

"""
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^getFps/', views.get_fps, name='fps_info'),
    url(r'^getMem/', views.get_memory, name='memory_info'),
    url(r'^getCpu/', views.get_cpu, name='cpu_info'),
    url(r'^getFlow/', views.get_flow, name='flow_info'),
    url(r'^getKpi/', views.get_kpi, name='kpi_info'),
    url(r'^getPower/', views.get_power, name='battery_info'),
]