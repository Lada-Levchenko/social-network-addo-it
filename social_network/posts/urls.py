from django.conf.urls import url
from rest_framework.compat import include

from .views import PostViewSet, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^like/(?P<pk>\d+)/$', LikePostView.as_view(), name='post-like'),
    url(r'^unlike/(?P<pk>\d+)/$', UnlikePostView.as_view(), name='post-unlike'),
]
