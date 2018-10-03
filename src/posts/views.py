from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.  C R U D - Create, retrieve, update, delete

def posts_create(request): #As create
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())#Redirects page after post create
	context = {
		"form" : form,
	}
	return render(request, "posts_form.html", context)

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

def posts_update(request, id=None): #As update
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())#Redirects page after post update
	context = {
	"title" : instance.title,
	"form" : form,
	"instance": instance
	}
	return render(request, "posts_form.html", context)

def posts_delete(request): #As delete
	return HttpResponse("<h1>Delete</h1>")
