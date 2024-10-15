from django.urls import path, include

urlpatterns = [
    path('authors/', include('core.api.authors.urls')),
    path('genres/', include('core.api.genres.urls')),
]