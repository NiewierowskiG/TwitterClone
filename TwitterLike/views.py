from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreatePost
from .models import Comment, Tweet, Retweet


def home_page(request):
    tweets = Tweet.objects.all().order_by('-pub_date')
    return render(request, 'TwitterLike/home.html', {"tweets": tweets})


def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if (form.is_valid()):
            Tweet.objects.create(author=request.user, desc=request.POST.get('desc'), img=request.POST.get('img'))
            return redirect('/twitter')
    else:
        form = CreatePost()
    return render(request, "TwitterLike/create_post.html", {"form": form})
