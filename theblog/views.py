from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Category, Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

#Post Views
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


# Category Views
# class CreateCategoryView(CreateView):
#     model = Category
#     template_name = ''
#     fields = ('name')
# template and url pattern not needed yet
