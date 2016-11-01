from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/index/')
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method =='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = PostForm(instance=post)
    return render(request, 'add_post.html', {'form': form})
