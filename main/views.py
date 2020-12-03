from django.shortcuts import render , HttpResponse
from .models import *
# Create your views here.
def posts(request):

	posts = post.objects.all()

	return render(request, 'posts.html' , {'posts' : posts})

def post_detail(request, pk):

	posts = post.objects.get(pk=pk)

	return render(request, 'post_detail.html', {'post': posts})	