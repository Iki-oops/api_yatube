from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

PREFIX = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('posts/(?P<post_id>[0-9]+)/comments', CommentViewSet,
                basename='comment')

urlpatterns = [
    path(f'{PREFIX}/v1/', include(router.urls)),
    path(f'{PREFIX}/v1/api-token-auth/', views.obtain_auth_token),
]
