from django.shortcuts import render
from .models import Post


def blog_index(request):
    blogs = Post.objects.order_by('-created_on')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)