from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/', include('api.inner', namespace='api')),
]
