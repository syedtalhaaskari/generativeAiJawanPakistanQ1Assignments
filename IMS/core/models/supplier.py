from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
