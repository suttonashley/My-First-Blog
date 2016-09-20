from django.shortcuts import render
#importing timezone because we are using it in our 'posts' QuerySet.
from django.utils import timezone
# Here we are importing the models we want to include in out template into our views.py
from .models import Post


# Create your views here.

# So your views is like your controller in the sense that it looks to the views.py folder after a request for post_list url is made...
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
