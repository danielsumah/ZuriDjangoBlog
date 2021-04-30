# Main Blog views modules
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
# Access Modules
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#  Form creation module
from .forms import CreateUserForm, CreateProductForm
# Models
from .models import Post
from.models import Comment


# Create your views here.
# @method_decorator(login_required)

class BlogCommentView(ListView):
    model = Comment
    template_name = 'post_comment_view.html'
    

def blog_list_view(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)



def blog_detail_view(request, my_id):
    # posts = Post.objects.get(id=my_id)
    posts = get_object_or_404(Post, id=my_id)
    
    context = {
        'post': posts
    }
    return render(request, 'post_detail.html', context)


# class BlogCreateView(CreateView):
#     model = Post
#     template_name = 'post_new.html'
#     fields = ['title', 'author', 'body']

def blog_create_view(request):
    form = CreateProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = CreateProductForm()
            # messages.success(request, 'New Product Created')
            # return redirect('post_detail')
            
    context = {'form': form}
    return render(request, 'post_new.html', context)


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


