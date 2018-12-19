from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet


router = DefaultRouter()
router.register(r'api/users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'', include(router.urls)),

]