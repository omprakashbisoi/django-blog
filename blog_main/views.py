from django.shortcuts import render
from blogs.models import Category,Blog
from assignment.models import About
def home(request):
    featured_posts = Blog.objects.filter(is_featured = True,status = 1).order_by('updated_at')
    normal_posts = Blog.objects.filter(is_featured = False,status = 1).order_by('updated_at')
    try:
        about = About.objects.all()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'normal_posts': normal_posts,
        'about': about,

    }
    return render(request,'home.html',context)