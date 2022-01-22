from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
from django.db.models.aggregates import StdDev
from api.models import Property
from rest_framework.response import Response
from api.serializers import PropertySerializer


# https://www.youtube.com/watch?v=Ue52N-eu9MM APIViews

# Create your views here.

class PropertyList(generics.ListCreateAPIView):
    """
    Retrieves and updates a list of all the properties or with a certain longitude and latitude.

        Is it just me or is this vague

        "to retrieve, update, and delete all properties with the same longitude and
        latitude;"
    """
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        # Filtering on longitude and latitude
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')
        if longitude is not None:
            queryset = queryset.filter(longitude=longitude)
        elif latitude is not None:
            queryset = queryset.filter(latitude=latitude)
        return queryset


class _property(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, retrieves and deletes specific property by its externalId
    """
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    lookup_field = 'externalId'


class City(generics.ListAPIView):
    """
    Retrieves all properties in a city where isRoomActive = True optionally filtered and within a rent budget
    """
    serializer_class = PropertySerializer
    filter_backends = [filters.OrderingFilter]
    pagination_class = PageNumberPagination
    # Fields that are used when ordering is specified
    # http://example.com/api/users?ordering=account for example
    #ordering_fields = ['rent', 'costPerSqm']

    # LOL thank you random guy from stackOverFlow!
    # https://stackoverflow.com/questions/46282173/django-ordering-by-property-field
    # Default ordering is by rent
    # ordering = ['rent']

    def get_queryset(self):
        city = self.kwargs['city']
        # Slicing of the queryset is not allowed after ordering
        # How to fix this?
        numResults = 10  # Default value for the amount of results
        # queryset = Property.objects.filter(city=city).order_by(orderDir + orderBy)
        queryset = Property.objects.filter(city=city)
        # Getting filtering parameters form the URL
        minRent = self.request.query_params.get('min-rent')
        maxRent = self.request.query_params.get('max-rent')
        # Checking if they are present
        if minRent is not None:
            queryset = queryset.filter(rent__gte=minRent)

        if maxRent is not None:
            queryset = queryset.filter(rent__lte=maxRent)

        # Check if number of results is specified
        if self.request.query_params.get('num-results') is not None:
            numResults = int(self.request.query_params.get('num-results'))
        # Figure out a way to slice AND use the build in orderby methods!
        if self.request.query_params.get('order-by') is not None:
            queryset = queryset.order_by(self.request.query_params.get('order-by'))
        return queryset


@api_view()
def statistics(request, city):
    queryset = Property.objects.filter(city=city)
    mean_rent = queryset.aggregate(Avg('rent'))
    count = queryset.count()
    median_rent = queryset.values_list('rent', flat=True).order_by('rent')[int(round(count/2))]
    std_rent = Property.objects.filter(city=city).aggregate(StdDev("rent"))
    mean_deposit = Property.objects.filter(city=city).aggregate(Avg('deposit'))
    median_deposit = queryset.values_list('deposit', flat=True).order_by('rent')[int(round(count / 2))]
    std_deposit = Property.objects.filter(city=city).aggregate(StdDev("rent"))

    return Response({"mean_rent":mean_rent,
                     "median_rent": median_rent,
                     "std_rent": std_rent,
                     "mean_deposit": mean_deposit,
                     "median_deposit": median_deposit,
                     "std_deposit": std_deposit
                     })
# class Statistics(AP)
