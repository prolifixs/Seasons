from django.conf.urls import url
from django.contrib import admin
from .views import (
	posts_create,
	posts_detail,
	posts_list,
	posts_update,
	posts_delete,
	)

#custom urls for specific app "posts". this is to make the global url file more dynamic in search
urlpatterns = [
    url(r'^$', posts_list),
    url(r'^create/$', posts_create),#url(r'^$', "<appname>.view_module.<function_name>")
    url(r'^detail/$', posts_detail),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete),
]
