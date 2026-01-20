from django.urls import path
from . import views
urlpatterns = [
    #category crud
    path('',views.dashboard,name = 'dashboard'),
    path('category/',views.categories,name = 'categories'),
    path('category/add/',views.add_category,name="add_category"),
    path('category/edit/<int:pk>/',views.edit_category,name="edit_category"),
    path('category/delete/<int:pk>/',views.delete_category,name="delete_category"),
    #post crud
    path('posts/',views.posts,name="posts"),
    path('posts/add/',views.add_posts,name="add_posts"),
    path('posts/edit/<int:pk>/',views.edit_posts,name="edit_posts"),
    path('posts/delete/<int:pk>/',views.delete_posts,name="delete_posts"),
]