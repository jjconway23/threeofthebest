from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Category, Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

#Post Views
class ListHomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id',]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ListHomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DetailPostView(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


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

def ListAllCategoriesView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list': cat_menu_list})

def ListCategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(request, 'categories.html', {'cats': cats.title().replace("-", " "), 'category_posts': category_posts})

# class CreateCategoryView(CreateView):
#     model = Category
#     template_name = ''
#     fields = ('name')
# template and url pattern not needed yet
