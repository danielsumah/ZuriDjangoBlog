# Main Blog views modules
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Access Modules
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#  Form creation module
from .forms import CreateUserForm
# Models
from .models import Post
from.models import Comment


# Create your views here.
# @method_decorator(login_required)

class BlogCommentView(ListView):
    model = Comment
    template_name = 'post_comment_view.html'
    
class BlogListView(ListView):
    # login_url = '/blog_login/'
    # redirect_field_name = 'home'

    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def blog_register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('blog_login')

    context = {'form': form}
    return render(request, 'register.html', context)


def blog_login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect ')

    context = {}
    return render(request, 'login.html', context)


def blog_logout(request):
    logout(request)
    return redirect('blog_login')


