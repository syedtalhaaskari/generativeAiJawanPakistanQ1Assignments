from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, LogoutAPIView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
] + router.urls