from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from users import urls as users_urls, api_urls as users_api_urls
from photos import urls as photos_urls, api_urls as photos_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    #Users URLS
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls)),

    #Photos URLS
    url(r'', include(photos_urls)),
    url(r'api/', include(photos_api_urls))

]
