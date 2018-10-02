from django.conf.urls import url
from django.contrib import admin
from . import views

#custom urls for specific app "posts". this is to make the global url file more dynamic in search
urlpatterns = [
    url(r'^create/$', "posts.views.posts_create"),#url(r'^$', "<appname>.view_module.<function_name>")
    url(r'^detail/$', "posts.views.posts_detail"),
    url(r'^$', "posts.views.posts_list"),
    url(r'^update/$', "posts.views.posts_update"),
    url(r'^delete/$', "posts.views.posts_delete"),
]
