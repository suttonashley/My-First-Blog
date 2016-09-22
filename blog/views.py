from django.shortcuts import render, get_object_or_404
#importing timezone because we are using it in our 'posts' QuerySet.
from django.utils import timezone
# Here we are importing the models we want to include in out template into our views.py
from .models import Post

from .views import PostForm


# Create your views here.

# So your views is like your controller in the sense that it looks to the views.py folder after a request for post_list url is made...
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts} )

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post' : post})

def post_view(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
