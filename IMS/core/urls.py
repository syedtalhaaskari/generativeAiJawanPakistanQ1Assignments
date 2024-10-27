from django.urls import path

from .views.category import get_or_create_category, get_or_update_or_delete_category
from .views.supplier import get_or_create_supplier, get_or_update_or_delete_supplier
from .views.product import get_or_create_product, get_or_update_or_delete_product

urlpatterns = [
    path('categories/', get_or_create_category),
    path('categories/<int:id>/', get_or_update_or_delete_category),
    path('suppliers/', get_or_create_supplier),
    path('suppliers/<int:id>/', get_or_update_or_delete_supplier),
    path('products/', get_or_create_product),
    path('products/<int:id>/', get_or_update_or_delete_product),
]