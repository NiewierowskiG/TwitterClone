from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreatePost
from .models import Comment, Tweet, Retweet
from django.http import Http404
from django.contrib.auth.decorators import login_required


def home_page(request):
    if request.GET.get('liked'):
        if not request.user.is_authenticated:
            return redirect('/login')
        tweet = Tweet.objects.filter(id=(request.GET.get('tweet_id')))[0]
        tweet.likes.add(request.user)
    if request.GET.get('unliked'):
        tweet = Tweet.objects.filter(id=(request.GET.get('tweet_id')))[0]
        tweet.likes.remove(request.user)
    if request.GET.get('retweet'):
        tweet = Tweet.objects.filter(id=(request.GET.get('tweet_id')))[0]
        retweet = Retweet.objects.create(author=request.user, tweet=tweet)
    tweets = Tweet.objects.all().order_by('-pub_date')
    user = request.user
    return render(request, 'TwitterLike/home.html', {"tweets": tweets, "user": user})


@login_required()
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            Tweet.objects.create(author=request.user, desc=form.cleaned_data.get('desc'), img=form.cleaned_data.get('img'))
            return redirect('/twitter')
    else:
        form = CreatePost()
    return render(request, "TwitterLike/create_post.html", {"form": form})


def single_tweet(request, pk):
    tweet = Tweet.objects.filter(id=pk)[0]
    if request.GET.get('liked'):
        if not request.user.is_authenticated:
            return redirect('/login')
        tweet.likes.add(request.user)
    if request.GET.get('unliked'):
        tweet.likes.remove(request.user)
    if request.GET.get('liked-comment'):
        if not request.user.is_authenticated:
            return redirect('/login')
        comment = Comment.objects.get(id=(request.GET.get('comment_id')))
        comment.likes.add(request.user)
    if request.GET.get('unliked-comment'):
        comment = Comment.objects.get(id=(request.GET.get('comment_id')))
        comment.likes.remove(request.user)
    if request.GET.get('retweet'):
        tweet = Tweet.objects.filter(id=(request.GET.get('tweet_id')))[0]
        retweet = Retweet.objects.create(author=request.user, tweet=tweet)
    return render(request, "TwitterLike/single_tweet.html", {"tweet": tweet, "user": request.user})


@login_required()
def create_comment(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            Comment.objects.create(author=request.user, desc=form.cleaned_data.get('desc'), img=form.cleaned_data.get('img'),
                                   tweet=Tweet.objects.get(id=pk))
            return redirect(f'/twitter/{pk}')
    else:
        form = CreatePost()
    return render(request, "TwitterLike/create_comment.html", {"form": form})


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(author=user)
        retweets = Retweet.objects.filter(author=user)
        tweet_list = list(tweets) + list(retweets)
        tweet_list.sort(key=lambda x: x.pub_date, reverse=True)
    except User.DoesNotExist:
        raise Http404
    return render(request, "TwitterLike/user_page.html", {"user": user, "tweet_list": tweet_list})
