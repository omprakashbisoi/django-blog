from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.template.defaultfilters import slugify

# Create your views here.

@login_required(login_url='login')
def dashboard(requeset):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        "category_count":category_count,
        "blog_count":blog_count,
    }
    return render(requeset,"dashboards/dashboard.html",context)

def categories(request):
    return render(request,'dashboards/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboards/add_categories.html',context)

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request,'dashboards/edit_categories.html',context)
def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'dashboards/posts.html',context)
def add_posts(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) +'-'+ str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = BlogForm()
    
    context ={
        'form':form,
    }
    return render(request,'dashboards/add_posts.html',context)
    
def edit_posts(request,pk):
    posts = get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=posts)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) +'-'+ str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = BlogForm(instance=posts)
    context = {
        'form':form,
        'posts':posts,
    }
    return render(request,'dashboards/edit_posts.html',context)

def delete_posts(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')