from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about/', views.about, name='about'),
]
