from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
