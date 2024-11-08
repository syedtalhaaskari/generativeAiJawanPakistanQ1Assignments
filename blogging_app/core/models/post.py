from django.db import models
from django.contrib.auth.models import User

from .category import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="posts_owner", on_delete=models.CASCADE)
    authors = models.ManyToManyField(User, related_name="posts")
    category = models.ManyToManyField(Category, related_name="posts")

    def __str__(self):
        return f"{self.id} - {self.title}"