from django.shortcuts import render,redirect
from blogs.models import Blog
from assignment.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import auth
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

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,"register.html",context)

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"login- {username}")
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect("home")
