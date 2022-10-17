from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

class ListHomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class DetailPostView(DetailView):
    model = Post
    template_name = 'blog_details.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

