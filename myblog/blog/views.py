from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from random import choice

from .models import Blog
from .forms import BlogForm, NewUserForm

_entries_per_page = 5


# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-id')
    while True:
        try:
            rand_id = choice(blogs).id
            break
        except IndexError:
            pass
    paginator = Paginator(blogs, _entries_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'rand_entry': rand_id,
        'page_obj': page_obj,
    }
    return render(request, 'blog/home.html', context)


def blog_post(request, id=1):
    blogs = Blog.objects.all().order_by('-id')
    while True:
        try:
            rand_id = choice(blogs).id
            break
        except IndexError:
            pass
    blog_post = Blog.objects.get(id=id)
    context = {
        'blog': blog_post,
        'rand_entry': rand_id,
    }
    return render(request, 'blog/blog_post.html', context)


def blog_create(request):
    blogs = Blog.objects.all().order_by('-id')
    while True:
        try:
            rand_id = choice(blogs).id
            break
        except IndexError:
            pass
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            print("form is valid.")
            new_blog = form.save(commit=False)
            new_blog.title = form.cleaned_data['title']
            new_blog.body = form.cleaned_data['entry']
            new_blog.author = request.user
            new_blog.save()
            return HttpResponseRedirect('/blog/' + str(new_blog.id))
        else:
            form.errors
    else:
        form = BlogForm()

    context = {
        'form': form,
        'rand_entry': rand_id,
    }
    return render(request, 'blog/create.html', context)


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('/')
        messages.error(
            request,
            'Unsuccessful registration. Invalid information.'
        )
    form = NewUserForm()
    context = {'register_form': form}
    return render(
        request,
        'blog/register.html',
        context,
    )


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'blog/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')
