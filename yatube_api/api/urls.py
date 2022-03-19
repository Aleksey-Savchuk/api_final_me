"""urls_api."""

from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet
# , FollowViewSet

app_name = 'api'


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register(r'groups', GroupViewSet, basename='groups')
# router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('api/v1/', include(router_v1.urls)),
]
