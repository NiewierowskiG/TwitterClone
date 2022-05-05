from django.contrib import admin
from .models import Tweet, Retweet, Comment

admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Comment)
