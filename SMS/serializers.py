from rest_framework import serializers
from .models import SMS, SMSTemplate, CustomerSMS

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = [
            'header',
            'created_date',
            'modified_date',
            'created_by',
            'modified_by'
        ]
        read_only_fields = ['id']

class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = [
            'message_template',
            'created_date',
            'modified_date',
            'created_by',
            'modified_by',
            'language',
            'sms',
            ]
        read_only_fields = ['id']


class CustomerSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = [
            'sms_template',
            'customer',
            'sent_date',
            'promo_code',
            'message',
            ]
        read_only_fields = ['id']

