# blog/urls.py - CORRECT ORDER

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # The specific path for creating a new post comes FIRST.
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    # The dynamic path for viewing a post comes AFTER.
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]