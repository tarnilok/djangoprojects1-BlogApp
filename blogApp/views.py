from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from .forms import UserForm, NewPost
from .models import User, Post, Likes, Comments
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def navbar(request):
    return render(request, 'blogApp/navbar.html')

def home_page(request):
    posts = get_list_or_404(Post)
    context = {
        'posts' : posts
    }
    return render(request, 'blogApp/home.html', context)

def about_page(request):
    return render(request, 'blogApp/about.html')

@login_required()
def create_post(request):
    form = NewPost()
    if request.method == "POST":
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_owner = request.user
            post.save()
            if post.status  == 'Draft':
                messages.success(request, 'saved as a draft')
            else:
                messages.success(request, 'Your Post has been published👍')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Form! Please try again!')
    context = {
        'form' : form
    }
    return render(request, 'blogApp/post_create.html', context)

def detail_post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post' : post
    }
    return render(request, 'blogApp/post_detail.html', context)

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = NewPost(instance=post)
    if request.method == "POST":
        form = NewPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Form! Please try again!')
    context = {
        'form' : form,
        'post' : post
    }
    return render(request, 'blogApp/post_update.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'The post has been deleted!')
        return redirect('home')
    context = {
        'post' : post
    }
    return render(request, 'blogApp/post_delete.html', context)

def post_comments(request):
    return render(request, 'blogApp/post_comments.html')
    
def user_profile(request, id):
    posts = get_list_or_404(Post)
    user_info = get_object_or_404(User, id=id)
    context = {
        'user_info' : user_info,
        'posts' : posts
    }
    return render(request, 'blogApp/user_profile.html', context)

def user_update(request, id):
    user_info = get_object_or_404(User, id=id)
    form = UserForm(instance=user_info)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Form! Please try again!')
            
    context = {
        'user_info' : user_info,
        'form' : form
    }
    return render(request, 'blogApp/user_update.html', context)

def user_register(request):
    form = UserForm()   
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            photo = form.cleaned_data['user_image']
            name = form.cleaned_data['name']
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password, name=name, photo=photo)
            messages.success(request, 'Registered successfully')
            return redirect('login')
        else :
            messages.error(request, "Registration failed")
            
    context = {
        'register_form' : form
    }
    return render(request, 'blogApp/register_page.html', context)
            
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, 'Login successfully')
            login(request, user)
            return redirect('home')
    context = {
        'login_form' : form
    }
    return render(request, 'blogApp/login_page.html', context)

def user_logout(request):
    messages.success(request, 'Logout successfully')
    logout(request)
    return redirect('home')
