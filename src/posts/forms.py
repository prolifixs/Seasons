from django import forms
from .models import Post

class PostForm(forms.ModelForm):#To be used in create viev
	class Meta:	
		model = Post
		fields = [
			"title",
			"context",
			"image"
		]