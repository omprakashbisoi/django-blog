from  .models import Category
from assignment.models import SocialLink
def get_category(request):
    categorires = Category.objects.all()
    return dict(categorires=categorires)

def get_social_link(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)