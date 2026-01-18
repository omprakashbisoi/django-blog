from django.shortcuts import render,get_object_or_404
from .models import Blog,Category
from django.db.models import Q
# Create your views here.

def posts_by_category(request,category_id):
    posts_featured = Blog.objects.filter(status = 1,is_featured = True,pk =category_id).order_by('updated_at')
    # normal_posts = Blog.objects.filter(status = 1,is_featured = False,pk =category_id).order_by('updated_at')
    category = get_object_or_404(Category,pk=category_id)
    context = {
        "posts_featured":posts_featured,
        'category':category
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_object = get_object_or_404(Blog,slug=slug,status=1)
    context = {
        'single_object':single_object,
    }
    return render(request,'blogs.html',context)

from django.db.models import Q

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword) |
        Q(blog_body__icontains=keyword),
        status=1
    )

    context = {
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "search.html", context)


