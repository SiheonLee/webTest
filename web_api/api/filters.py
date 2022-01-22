# https://www.youtube.com/watch?v=G-Rct7Na0UQ
import django_filters

from .models import Property


class PropertyExternalIdFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ('property_externalID',)


class PropertyLonLatFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ('location_latitude', 'location_longitude',)