from django.conf.urls import url
from rest_framework.compat import include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserValidCreateView, UserInvalidCreateView, UserAdditionalDataView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^users/token-auth/', obtain_jwt_token, name='user-token-auth'),
    url(r'^users/token-refresh/', refresh_jwt_token, name='user-token-refresh'),
    url(r'^users/token-verify/', verify_jwt_token, name='user-token-verify'),       # don't know whether it's needed
    url(r'^users/register/$', UserValidCreateView.as_view(), name='user-register'),
    url(r'^users/register-invalid/$', UserInvalidCreateView.as_view(), name='user-register-invalid'),
    url(r'^users/additional-data/$', UserAdditionalDataView.as_view(), name='user-additional-data'),
    url(r'^', include(router.urls)),
]
