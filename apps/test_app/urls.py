from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^goback$', views.goback),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]
