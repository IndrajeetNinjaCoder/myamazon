from os import times
from sqlite3 import paramstyle
from turtle import pos
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.
def index(request):
    blogPosts = Blogpost.objects.all()
    # print(blogPosts)
    params = {'blogPosts': blogPosts}
    return render(request, 'blog/index.html', params)

def blogpost(request, postid):
    post = Blogpost.objects.filter(post_id=postid)
    n = len(Blogpost.objects.all())
    prevPost = nextPost = post
    prev = next = False

    if postid > 1:
        prevPost = Blogpost.objects.filter(post_id=postid-1)
        prev = True
    if postid < n:
        nextPost = Blogpost.objects.filter(post_id=postid+1)
        next = True

    params = {'postid': postid, 'post':post[0], 'prevPost': prevPost[0], 'nextPost': nextPost[0], 'prev':prev, 'next':next}

    return render(request, 'blog/blogpost.html', params)

