from django.shortcuts import render
from blogs.models import Category,Blog
def home(request):
    featured_posts = Blog.objects.filter(is_featured = True,status = 1).order_by('updated_at')
    normal_posts = Blog.objects.filter(is_featured = False,status = 1).order_by('updated_at')
    context = {
        'featured_posts': featured_posts,
        'normal_posts': normal_posts,

    }
    return render(request,'home.html',context)