from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Category, Post, Comment, SubCategory,Product
from .forms import PostForm, UpdatePostForm, UpdateCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
import random
from decouple import config
from django.core.mail import send_mail


def ListHomeView(request):
    posts = Post.objects.all().order_by('-id')
    cat_menu = Category.objects.all()
    sub_cats = SubCategory.objects.all()
    comments = Comment.objects.all()
    home_comments = random.choices(comments, k=5)
    return render(request, 'home.html', {
            'posts':posts,
            'cat_menu': cat_menu,
            'sub_cats': sub_cats,
            'home_comments': home_comments,
        })

def ListAllPostsView(request):
    posts = Post.objects.all()
    p = Paginator(posts, 13)
    page = request.GET.get('page')
    all_posts_list = p.get_page(page)
    nums = 'J' * all_posts_list.paginator.num_pages

    return render(request, 'all_blog_post_list.html',{
        'all_posts_list': all_posts_list,
        'nums': nums,

    })

class DetailPostView(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()

        post_wanted = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_wanted.total_likes()
        liked = False
        if post_wanted.likes.filter(id=self.request.user.id).exists():
            liked = True


        context = super(DetailPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
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
def ListAllSubCategoriesView(request, slug):
    sub_category = SubCategory.objects.get(slug=slug) 
    posts = Post.objects.all()
    post_with_slug = Post.objects.filter(sub_category__exact=sub_category).count() == 0

    p = Paginator(posts, 13)
    page = request.GET.get('page')
    all_posts = p.get_page(page)
    nums = 'J' * all_posts.paginator.num_pages

    return render(request, 'sub_categories_list.html',{
        'posts': posts,
        'sub_category': sub_category,
        'all_posts': all_posts,
        'nums': nums,
        'posts': posts,
        'post_with_slug': post_with_slug,

    })

def ListAllCategoriesView(request):
    cat_menu_list = Category.objects.all()
    p = Paginator(cat_menu_list, 8)
    page = request.GET.get('page')
    all_categories = p.get_page(page)
    nums = 'J' * all_categories.paginator.num_pages
    sub_categories = SubCategory.objects.all()

    return render(request, 'categories_list.html',{
        'cat_menu_list': cat_menu_list, 
        'all_categories':all_categories, 
        'nums':nums, 
        'sub_categories':sub_categories,

    })

def ListCategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    p = Paginator(Post.objects.filter(category=cats.replace("-", " ")), 13)
    page = request.GET.get('page')
    categors = p.get_page(page)
    nums = 'J' * categors.paginator.num_pages

    return render(request, 'categories.html', 
                    {   'cats': cats.title().replace("-", " "), 
                        'category_posts': category_posts, 
                        'categors' : categors, 
                        'nums': nums,
    })

# Like Views

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))


# Comment View
class CreateCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = UpdateCommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs['pk']})


# Error Handling Page Views
def handle_not_found(request,exception):
    """ Handles 404 Error """
    return render(request,'not_found.html')

def handle_bad_error(request,exception):
    """Handles 400 Error """
    return render(request,'bad_error.html')

def handle_unauthorized_access(request,exception):
    """Handles 401 Error """
    return render(request,'unauthorized_access.html')

def handle_unexpected_condition(request):
    """Handles 500 Error """
    return render(request,'unexpected_condition.html')

def handle_server_unavailable(request,exception):
    """Handles 503 Error"""
    return render(request,'server_unavailable.html')

def handle_temporary_error(request,exception):
    """Handles 504 Error"""
    return render(request,'temporary_error.html')

# About Us Terms and Conditions
def about_us(request):
    return render(request, 'about_us.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def contact_us(request):
    if request.method == "POST":
        contact_full_name = request.POST['contact-full-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']
        to = config('USER_EMAIL')

        send_mail(
            'Support Query from {}'.format(contact_full_name),
            contact_message + " Email sent by {}".format(contact_email),
            contact_email,
            [to],
        )
        return render(request, 'home.html', {'contact_full_name': contact_full_name})
    
    else:
        return render(request, 'contact_us.html')