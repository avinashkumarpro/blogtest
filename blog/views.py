from django.shortcuts import render
from .models import Post 
from django.utils import timezone


def post_list(request):
	posts = Post.objects.filter(publihsed_date__lte=timezone.now()).order_by('publihsed_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
