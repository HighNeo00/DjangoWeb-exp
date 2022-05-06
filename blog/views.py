from django.shortcuts import render
from .models import Comment, Post

# Create your views here.


def post(request,id):
    p = Post.objects.get(id=id)
    c = Comment.objects.filter(post=p)
    context = {
        "comment": c,
        "post": p,
        "username": "Arash Ghazali"
    }
    return render(request, 'blog/post.html', context)


def index(request):
    return render(request, 'blog/index.html', {})


def posts(request):
    return render(request, 'blog/posts.html', {})
