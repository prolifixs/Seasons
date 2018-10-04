from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .forms import PostForm
from django.contrib import messages
from .models import Post

# Create your views here.  C R U D - Create, retrieve, update, delete

def posts_create(request): #As create
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "post created successfully")
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
	queryset_list = Post.objects.all()#.order_by("-timestamp")#Query for retrieving data from database
	paginator = Paginator(queryset_list, 12) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
	"object_lists": queryset,
	"title" : "List",
	"page_request_var" : page_request_var
	}
	return render(request, "post_list.html", context)
	#return HttpResponse("<h1>Lists</h1>")

def posts_update(request, id=None): #As update
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "post changed successfully")
		return HttpResponseRedirect(instance.get_absolute_url())#Redirects page after post update
	else:
		messages.error(request, "something went wrong")
	context = {
	"title" : instance.title,
	"form" : form,
	"instance": instance
	}
	return render(request, "posts_form.html", context)

def posts_delete(request, id=None): #As delete
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "post deleted")
	return redirect("posts:list")
