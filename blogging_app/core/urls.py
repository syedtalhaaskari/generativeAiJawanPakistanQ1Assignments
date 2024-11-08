from rest_framework.routers import DefaultRouter

from .views.category import CategoryViewSet
from .views.post import PostViewSet
from .views.comment import CommentViewSet
from .views.like import LikeViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)

urlpatterns = [] + router.urls