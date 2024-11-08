from django.db import models
from django.contrib.auth.models import User

from .post import Post
from .comment import Comment

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'comment')
