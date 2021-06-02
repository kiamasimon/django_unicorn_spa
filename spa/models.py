from django.contrib.auth.models import User
from django.db import models


class SupportTicket(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='comment_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

