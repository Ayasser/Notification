from rest_framework import serializers
from .models import Language, City, Customer, CustomerDevices

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'language',
        ]
        read_only_fields = ['id']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name_en',
            'name_ar',
            ]
        read_only_fields = ['id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'phone_number',
            'email',
            'city',
            'language',
            ]
        read_only_fields = ['id']

class CustomerDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDevices
        fields = [
            'customer',
            'device_id',
            'created_date',
        ]
        read_only_fields = ['id']