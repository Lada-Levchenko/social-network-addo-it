from django.conf.urls import url
from .views import PostCreateView, PostRetrieveView, PostUpdateView, \
    PostDeleteView, PostListView, LikePostView, UnlikePostView

urlpatterns = [
    url(r'^create/$', PostCreateView.as_view()),
    url(r'^get/(?P<pk>\d+)/$', PostRetrieveView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^list/$', PostListView.as_view()),
    url(r'^like/(?P<pk>\d+)/$', LikePostView.as_view(), name='post-like'),
    url(r'^unlike/(?P<pk>\d+)/$', UnlikePostView.as_view(), name='post-unlike'),
]
