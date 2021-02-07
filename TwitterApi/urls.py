"""
@Author: Vidhi Shah
@Purpose: It contains all the urls where page will be redirected when twitter api responses are received
"""
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('codes', views.callindex, name='index2'),
    path('sucess', views.succes, name='sucex'),
    path('login', views.loginmsg, name='loginmsg')
    ]