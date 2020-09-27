from django.shortcuts import render, get_object_or_404
from . models import Post
def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/list.html', {'post': post})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', publish__year=year, 
    publish__month = month, publish__day = day)
    return render(request, 'blog/detail.html', {'post':post})



