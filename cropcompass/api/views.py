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
)


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


class NassAnimalsSalesList(APIView):
    """
    List animal sales or create new instance.
    """
    def get(self, request, format=None):
        """List animal sales with optional filtering on year or commodity."""
        # Accepted fields for filtering output
        FILTERS = ['commodity', 'year']
        if request.query_params:
            # Build dictionary of filter parameters (exclude 'format', etc.)
            filter_params = {}
            for param in request.query_params.keys():
                vals = request.query_params.getlist(param)
                if param in FILTERS:
                    filter_params[param] = vals
            # Augment dictionary keys with __in for OR-ing values in the query
            query = {key + '__in': vals for key, vals in filter_params.items()}
            # Generate queryset
            animal_sales = NassAnimalsSales.objects.filter(**query)
        else:
            animal_sales = NassAnimalsSales.objects.all()
        serializer = NassAnimalsSalesSerializer(animal_sales, many=True)
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
        """Retrieve animal sales instance."""
        animal_sales = self.get_object(pk)
        serializer = NassAnimalsSalesSerializer(animal_sales)
        return Response(serializer.data)
