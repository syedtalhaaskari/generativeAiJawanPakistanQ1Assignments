from django.urls import path
from .views import get_or_create_author, get_or_update_or_delete_author

urlpatterns = [
    path('', get_or_create_author),
    path('<int:id>/', get_or_update_or_delete_author)
]