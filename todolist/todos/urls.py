from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from todos import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^details/(?P<id>\w{0,50})/$', views.details)

   ]

