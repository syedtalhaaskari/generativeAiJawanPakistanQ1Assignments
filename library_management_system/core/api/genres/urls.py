from django.urls import path
from .views import get_or_create_genre, get_or_update_or_delete_genre

urlpatterns = [
    path('', get_or_create_genre),
    path('<int:id>/', get_or_update_or_delete_genre)
]