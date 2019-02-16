from rest_framework import serializers
from .models import Notification, NotificationTemplate, CustomerNotification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'header',
            'created_date',
            'modified_date',
            'created_by',
            'modified_by'
        ]
        read_only_fields = ['id']

class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = [
            'notification_title',
            'notification_body', 
            'created_date',
            'modified_date',
            'created_by',
            'modified_by',
            'language',
            'notification',
            ]
        read_only_fields = ['id']


class CustomerNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerNotification
        fields = [
            'notification_template',
            'customer',
            'sent_date',
            'promo_code',
            'notification_title',
            'notification_body',
            ]
        read_only_fields = ['id']

