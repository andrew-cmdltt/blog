from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from posts.models import Post
from django.http import HttpResponse
from blog.helpers import Helpers
from .forms import PostAddForm, PostEditForm

class PostController():
    def addPost(request):
        if request.method == 'GET':
            form = PostAddForm()
            return render(request, 'posts/add.html', {"form": form})
        else:
            bound_form = PostAddForm(request.POST, request.FILES)
            if bound_form.is_valid():
                bound_form.save(request.user.pk)
                return HttpResponseRedirect('/')
            return render(request, 'posts/add.html', {"form": bound_form})

    def editPost(request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Exception as e:
            return render(request, 'mainApp/message.html', {"message": "Post not found"})
        form = PostEditForm(initial={
            'title': post.title,
            'description': post.description
        })
        if request.method == 'GET':
            return render(request, 'posts/edit.html', {"form": form})
        else:
            bound_form = PostEditForm(request.POST, request.FILES)
            if bound_form.is_valid():
                Helpers.editPost(post, request)
                return HttpResponseRedirect('/')
            return render(request, 'posts/edit.html', {"form": bound_form})

    def deletePost(request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Exception as e:
            return render(request, 'mainApp/message.html', {"message": "Post not found"})
        post.delete()
        return HttpResponseRedirect('/')

    def showPost(request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Exception as e:
            return render(request, 'mainApp/message.html', {"message": "Post not found"})
        return render(request, "posts/post.html", {"post": post})






