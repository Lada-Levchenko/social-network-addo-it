from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserView, AuthRegister, AuthLogin


urlpatterns = [
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),       # don't know whether it's needed
    url(r'^test/', UserView.as_view(), name='test'),
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^login/$', AuthLogin.as_view()),
]
