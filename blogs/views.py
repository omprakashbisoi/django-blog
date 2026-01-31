from django.shortcuts import render,get_object_or_404
from .models import Blog,Category,Comment
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def posts_by_category(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    posts_featured = Blog.objects.filter(is_featured = True,status = 1,category =category).order_by('updated_at')
    # normal_posts = Blog.objects.filter(status = 1,is_featured = False,pk =category_id).order_by('updated_at')
    context = {
        "posts_featured":posts_featured,
        'category':category
    }
    print(posts_featured)
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_object = get_object_or_404(Blog,slug=slug,status=1)
    comments = Comment.objects.filter(blog = single_object)
    comments_count = Comment.objects.filter(blog = single_object).count()
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_object
        comment.comment = request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'single_object':single_object,
        'comments':comments,
        'comments_count':comments_count,
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


