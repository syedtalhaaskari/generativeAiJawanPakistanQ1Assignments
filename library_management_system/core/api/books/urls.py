from django.urls import path
from .views import get_or_create_book, get_or_update_or_delete_book

urlpatterns = [
    path('', get_or_create_book),
    path('<int:id>/', get_or_update_or_delete_book)
]