from django.urls import path

from .views.category import get_or_create_category, get_or_update_or_delete_category, show_category_metrics
from .views.supplier import get_or_create_supplier, get_or_update_or_delete_supplier, show_supplier_metrics
from .views.product import get_or_create_product, get_or_update_or_delete_product, show_product_metrics, show_product_audit, show_product_audit_by_product_id

urlpatterns = [
    path('categories/', get_or_create_category),
    path('categories/<int:id>/', get_or_update_or_delete_category),
    path('categories/metrics/', show_category_metrics),
    path('suppliers/', get_or_create_supplier),
    path('suppliers/<int:id>/', get_or_update_or_delete_supplier),
    path('suppliers/metrics/', show_supplier_metrics),
    path('products/', get_or_create_product),
    path('products/<int:id>/', get_or_update_or_delete_product),
    path('products/metrics/', show_product_metrics),
    path('products/audit/', show_product_audit),
    path('products/audit/<int:id>/', show_product_audit_by_product_id),
]