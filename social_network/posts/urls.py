from django.conf.urls import url
from .views import PostCreateView, PostRetrieveView, PostUpdateView, \
    PostDeleteView, PostListView

urlpatterns = [
    url(r'^create/$', PostCreateView.as_view()),
    url(r'^get/(?P<pk>\d+)/$', PostRetrieveView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view()),
    url(r'^list/', PostListView.as_view()),
]
