from rest_framework import serializers
from .models import PromoCode

class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = [
            'code',
        ]
        read_only_fields = ['id']
