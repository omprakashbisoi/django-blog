from django.shortcuts import render,get_object_or_404
from .models import Blog,Category
# Create your views here.

def posts_by_category(request,category_id):
    posts_featured = Blog.objects.filter(status = 1,is_featured = True,pk =category_id)
    # normal_posts = Blog.objects.filter(status = 1,is_featured = False,pk =category_id).order_by('updated_at')
    category = get_object_or_404(Category,pk=category_id)
    context = {
        "posts_featured":posts_featured,
        # "normal_posts":normal_posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)

