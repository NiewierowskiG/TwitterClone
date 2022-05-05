from django.db import models
from django.conf import settings


class Tweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500)
    img = models.ImageField(blank=True, upload_to="tweet_images/")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    pub_date = models.DateTimeField(auto_now_add=True)

    def retweet_counter(self):
        return self.retweet_set.all().count()

    def comment_counter(self):
        return self.comment_set.all().count()


class Retweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500)
    img = models.ImageField(blank=True, upload_to="comment_images/")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
