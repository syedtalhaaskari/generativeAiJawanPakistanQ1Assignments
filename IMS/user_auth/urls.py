from rest_framework.urls import path

from .views import login_view, logout_view, create_or_get_users

urlpatterns = [
    path('users/', create_or_get_users, name="create_or_get_users"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]