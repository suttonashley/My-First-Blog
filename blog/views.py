from django.shortcuts import render

# Create your views here.

# So your views is like your controller in the sense that it looks to the views.py folder after a request for post_list url is made...
def post_list(request):
    return render(request, 'blog/post_list.html', {})
