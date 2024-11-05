from django.db import models

class ProductAudit(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    supplier_ids = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"