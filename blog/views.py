from django.shortcuts import render
from .models import Post

# Create your views here.

def blog_post(request):
    context={'posts': Post.objects.all()}
    return render(request,'blog/blog_list.html',context)

