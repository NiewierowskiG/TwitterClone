from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_page),
    path('create', views.create_post),
    path('<int:pk>', views.single_tweet),
    path('<int:pk>/comment', views.create_comment),
    path('<str:username>', views.user_page)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
