from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('create', views.create_post)
    ]
