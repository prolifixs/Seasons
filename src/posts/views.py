from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.  C R U D - Create, retrieve, update, delete

def posts_create(request): #As create
	return HttpResponse("<h1>Create</h1>")

def posts_detail(request, id): #As retrieve
	instance = get_object_or_404(Post, id=id)
	context = {
	"title" : instance.title,
	"instance": instance
	}
	return render(request, "posts_detail.html", context)

def posts_list(request): #As retrieve
	queryset = Post.objects.all()#Query for retrieving data from database
	context = {
	"object_lists": queryset,
	"title" : "List"
	}
	return render(request, "index.html", context)
	#return HttpResponse("<h1>Lists</h1>")

def posts_update(request): #As update
	return HttpResponse("<h1>Update</h1>")

def posts_delete(request): #As delete
	return HttpResponse("<h1>Delete</h1>")
