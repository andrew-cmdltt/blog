from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from posts.models import Post
from django.http import HttpResponse

class PostController():
    def index(request):
        if not request.user.is_authenticated:
            return render(request, 'mainApp/message.html', {"message": "You are not authorized"})
        posts = Post.objects.filter(owner_id=request.user.pk)
        return render(request, "mainApp/index.html", {"posts": posts})
    def addPost(request):
        if request.Method == 'GET':
            return render(request, "posts/add.html")
    def searchPosts(request):
        posts = Post.objects.filter(title__contains=request.GET['title'])
        return render(request, "mainApp/index.html", {"posts": posts})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "mainApp/register.html"
    
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "mainApp/login.html"
    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login")

