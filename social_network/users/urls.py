from django.conf.urls import url
from rest_framework.compat import include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserValidCreateView, UserInvalidCreateView, UserAdditionalDataView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),       # don't know whether it's needed
    url(r'^register/$', UserValidCreateView.as_view()),
    url(r'^register-invalid/$', UserInvalidCreateView.as_view()),
    url(r'^additional-data/$', UserAdditionalDataView.as_view()),
]
