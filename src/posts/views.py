from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.  C R U D - Create, retrieve, update, delete

def posts_create(request): #As create
	return HttpResponse("<h1>Create</h1>")

def posts_detail(request): #As retrieve
	return HttpResponse("<h1>Detail</h1>")

def posts_list(request): #As retrieve
	return HttpResponse("<h1>Lists</h1>")

def posts_update(request): #As update
	return HttpResponse("<h1>Update</h1>")

def posts_delete(request): #As delete
	return HttpResponse("<h1>Delete</h1>")
