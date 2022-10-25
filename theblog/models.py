from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.db.models import UniqueConstraint, Q

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class SubCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.ForeignKey(Category, on_delete=models.CASCADE, default='uncategorized', related_name='sub_category')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    tiktok_url = models.CharField(max_length=255, blank=True, null=True)
    snapchat_url = models.CharField(max_length=255, blank=True, null=True)
    youtube_url = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        """
            When adding a new post, this function will direct them to
            the newly added post. May not be used as do not intend to allow
            users to create their own accounts to post a blog post.
        """
        return reverse('home')


    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='3oftheBest')
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    snippet_image = models.ImageField(null=True, blank=True, upload_to="snippet-image/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    snippet = models.CharField(max_length=255)
    isFeatured = models.BooleanField(default=False)


    class Meta:
        """
            This is to only allow one post with isFeatured boolean field checked.
        """
        constraints = [
            UniqueConstraint(fields=['isFeatured'], condition=Q(isFeatured=True), name='isFeatured')
        ]


    def total_likes(self):
        return self.likes.count()

        
    def __str__(self):
        return f"{self.title} | {str(self.author).capitalize()}"

    def get_absolute_url(self):
        """
            When adding a new post, this function will direct them to
            the newly added post. May not be used as do not intend to allow
            users to create their own accounts to post a blog post.
        """
        return reverse('home')



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} |  {self.name}"