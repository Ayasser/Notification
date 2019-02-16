from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PromoCodeSerializer
from .models import PromoCode
# Create your views here.

class PromoCodeViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`PromoCode<Promo_code.models.PromoCode>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = PromoCode.objects.all()
    serializer_class= PromoCodeSerializer
