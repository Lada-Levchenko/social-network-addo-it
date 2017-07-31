from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserListView, UserCreateView, UserRetrieveView, UserUpdateView, UserDeleteView


urlpatterns = [
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),       # don't know whether it's needed
    url(r'^register/$', UserCreateView.as_view()),
    url(r'^get/(?P<pk>\d+)/$', UserRetrieveView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', UserUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', UserDeleteView.as_view()),
    url(r'^list/', UserListView.as_view()),
]
