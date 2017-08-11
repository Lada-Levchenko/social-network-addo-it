from django.conf.urls import url
from rest_framework.compat import include

from .views import PostViewSet, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^posts/like/(?P<pk>\d+)/$', LikePostView.as_view(), name='post-like'),
    url(r'^posts/unlike/(?P<pk>\d+)/$', UnlikePostView.as_view(), name='post-unlike'),
    url(r'^', include(router.urls)),
]
