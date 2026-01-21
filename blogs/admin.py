from django.contrib import admin
from .models import Category,Blog,Comment
# Register your models here.
class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','is_featured')
    search_fields = ('id','title','categoty__category_name')
    list_editable =('is_featured',)

admin.site.register(Category)
admin.site.register(Blog,AdminBlog)
admin.site.register(Comment)