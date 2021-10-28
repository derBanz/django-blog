from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from random import choice

from .models import Blog
from .forms import BlogForm

blogs = Blog.objects.all().order_by('-id')
num_entries = Blog.objects.filter().count()
_entries_per_page = 5


# Create your views here.
def home(request):
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
    while True:
        try:
            rand_id = choice(blogs).id
            break
        except IndexError:
            pass
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.title = form.cleaned_data['title']
            new_blog.body = form.cleaned_data['entry']
            new_blog.author = form.cleaned_data['author']
            new_blog.save()
            return HttpResponseRedirect('/blog/' + str(new_blog.get(id)))
        else:
            form.errors
    else:
        form = BlogForm()

    context = {
        'form': form,
        'rand_entry': rand_id,
    }
    return render(request, 'blog/create.html', context)
