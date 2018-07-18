from rest_framework import viewsets

from users.models import Configuration
from users.serializers import ConfigurationSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
