from django.contrib.auth.models import User, Group
from api.models import Metadata, NassAnimalsSales
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metadata
        fields = (
            'name',
            'description',
            'table_name',
            'unit',
            'field',
            'source_name',
            'source_link'
        )


class NassAnimalsSalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NassAnimalsSales
        fields = (
            'commodity',
            'year',
            'fips',
            'animals'
        )
