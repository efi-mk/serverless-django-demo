from rest_framework import serializers

from users.models import Configuration


class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuration
        fields = ('key', 'value')
