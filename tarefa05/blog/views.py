from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detalhe(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/listas_posts.html',{'posts: posts'})
