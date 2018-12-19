from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from photos.api import PhotoViewSet

router = DefaultRouter()
router.register(r'api/photos', PhotoViewSet)

urlpatterns = [

    # PHOTOS API URLS
    url(r'', include(router.urls)),
]