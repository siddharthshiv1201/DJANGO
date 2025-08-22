# blog/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView # Add CreateView
from .models import Post
from django.urls import reverse_lazy # Import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Import this for security

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# YEH NAYA VIEW ADD KAREIN
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'category', 'tags'] # Yeh fields form mein dikhengi
    success_url = reverse_lazy('post_list') # Post create hone ke baad yahan redirect hoga