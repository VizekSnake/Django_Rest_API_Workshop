from rest_framework import serializers
from showtimes.models import Cinema, Screening


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = ('name', 'city', 'movies')
