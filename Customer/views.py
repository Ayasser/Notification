from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LanguageSerializer, CitySerializer, CustomerSerializer, CustomerDevicesSerializer
from .models import Language, City, Customer, CustomerDevices

# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`Language<Customer.models.Language>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = Language.objects.all()
    serializer_class= LanguageSerializer

class CityViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`City<Customer.models.City>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = City.objects.all()
    serializer_class= CitySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`Customer<Customer.models.Customer>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer

class CustomerDevicesViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`CustomerDevices<Customer.models.CustomerDevices>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = CustomerDevices.objects.all()
    serializer_class= CustomerDevicesSerializer
