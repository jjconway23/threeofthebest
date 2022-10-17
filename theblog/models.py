from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='3oftheBest')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} | {str(self.author).capitalize()}"

    def get_absolute_url(self):
        """
            When adding a new post, this function will direct them to
            the newly added post. May not be used as do not intend to allow
            users to create their own accounts to post a blog post.
        """
        return reverse('post-details', args=(str(self.id)))