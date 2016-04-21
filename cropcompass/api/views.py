"""
API views.

The API serves the response in either browsable format, by default, or when
including a "format=api" query parameter, or in JSON format, when including
a "format=json" query parameter.

The list views that support optional filtering indicate that in their
docstrings. For those views filtering can be applied as follows.

A URL may optionally include query parameters to filter the
JSON response. Query parameter keys that cause filtering should be
one of the field names in the FILTER_FIELDS list. Any other key is
ignored. The corresponding value is exact matched against the field
value in every table row. Multiple "key=value" pairs may be provided,
in any order, including multiple values for the same key.
"""

from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Metadata, NassAnimalsSales
from .serializers import (
    UserSerializer,
    GroupSerializer,
    MetadataSerializer,
    NassAnimalsSalesSerializer,
    NassAnimalsSalesSerializerWrapped,
)


class FilteredAPIView(APIView):
    """
    APIView extended with filtered query dictionary generator method
    """
    @staticmethod
    def query_dict(query_params, filter_fields):
        # Build dictionary of filter parameters (exclude 'format', etc.)
        filter_params = {}
        for param in query_params.keys():
            if param in filter_fields:
                vals = query_params.getlist(param)
                filter_params[param] = vals
        # Augment dictionary keys with __in for looking up list inclusion
        query = {key + '__in': vals for key, vals in filter_params.items()}
        return query


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows metadata to be viewed or edited.
    """
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer


class NassAnimalsSalesList(FilteredAPIView):
    """
    List animal sales or create new instance.
    """
    def get(self, request, format=None):
        """List animal sales with optional filtering from nass_animals_sales.

        Example 1: GET /nass_animals_sales/
        Returns all rows of the table in browsable API format, which is the default format, also specifiable by the query parameter "format=api".

        Example 2:
        GET /nass_animals_sales/?year=1997&commodity=Bison&year=2002&format=json
        Returns rows of Bison from 1997 and 2002 in JSON format.
        """
        # Accepted fields for filtering output
        FILTER_FIELDS = ['commodity', 'year']
        if request.query_params:
            # Generate query filter dictionary
            query = self.query_dict(request.query_params, FILTER_FIELDS)
            # Generate queryset
            animal_sales = NassAnimalsSales.objects.filter(**query)
        else:
            animal_sales = NassAnimalsSales.objects.all()
        serializer = NassAnimalsSalesSerializerWrapped({
            "error": None,
            "rows": animal_sales.count(),
            "data": animal_sales
        })
        return Response(serializer.data)


class NassAnimalsSalesDetail(APIView):
    """
    Retrieve animal sales instance.
    """
    def get_object(self, pk):
        try:
            return NassAnimalsSales.objects.get(pk=pk)
        except NassAnimalsSales.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Retrieve animal sales instance from nass_animals_sales.

        Example 1:
        GET /nass_animals_sales/2803/
        Returns the item with the id of 2803.
        """
        animal_sales = self.get_object(pk)
        serializer = NassAnimalsSalesSerializer(animal_sales)
        return Response(serializer.data)
