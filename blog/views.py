from django.shortcuts import render, get_object_or_404
#importing timezone because we are using it in our 'posts' QuerySet.
from django.utils import timezone
# Here we are importing the models we want to include in out template into our views.py
from .models import Post

from .forms import PostForm

from django.shortcuts import redirect



# Create your views here.

# So your views is like your controller in the sense that it looks to the views.py folder after a request for post_list url is made...
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts} )

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # diff b/w this and post_new is that this includes an extra pk.
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # diff b/w this and post_new is that this includes an instance.
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk) # diff b/w this and post_new is that this includes an extra pk.
    else:
        form = PostForm(instance=post) # diff b/w this and post_new is that this includes an instance.
    return render(request, 'blog/post_edit.html', {'form': form})
