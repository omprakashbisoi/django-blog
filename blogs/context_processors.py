from  .models import Category
def get_category(request):
    categorires = Category.objects.all()
    return dict(categorires=categorires)