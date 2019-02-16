from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firebase_admin import messaging

from Customer.models import Customer, CustomerDevices
from Promo_code.models import PromoCode
from .models import Notification, NotificationTemplate, CustomerNotification
from .serializers import NotificationSerializer, NotificationTemplateSerializer, \
    CustomerNotificationSerializer

# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`Notification<Push_Notification.models.Notification>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = Notification.objects.all()
    serializer_class= NotificationSerializer


class NotificationTemplateViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`NotificationTemplate<Push_Notification.models.NotificationTemplate>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = NotificationTemplate.objects.all()
    serializer_class= NotificationTemplateSerializer


class CustomerNotificationViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`CustomerNotification<Push_Notification.models.CustomerNotification>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = CustomerNotification.objects.all()
    serializer_class= CustomerNotificationSerializer

@api_view(['GET'])
def send_notification(request):
    """
    | Send Notification using Firebase to one or group of customer.

        parameters : 
        -customer_ids: Customer
        -notification_id : Notification
        -promo_code_id : PromoCode
    """
    if request.method == 'GET':
        
        customer_ids = request.query_params.get('customer_ids')
        if customer_ids:
            customer_ids = customer_ids.split(",")
        
        notification_id = request.query_params.get('notification_id')
        promo_code_id = request.query_params.get('promo_code_id')

        if notification_id is None or customer_ids is None:
            return Response("Pleas Send notification_id and customer_ids ", status=status.HTTP_404_NOT_FOUND)
        notification = Notification.objects.filter(id=notification_id).first()
        
        keys_dict = dict()
        promo_code = None
        if promo_code_id:
            promo_code = PromoCode.objects.filter(id=promo_code_id).first()
            if promo_code:
                keys_dict['[promo_code]'] = promo_code.code
        
        customers = Customer.objects.filter(id__in=customer_ids).order_by('language')
        if not customers or not notification:
            return Response("Cutomer or Notifiction not found", status=status.HTTP_404_NOT_FOUND)
        
        for customer in customers:
            notification_temp = NotificationTemplate.objects.filter(notification__id=notification.id,language__id=customer.language.id).first()
            body = notification_temp.notification_body
            title = notification_temp.notification_title
            keys_dict['[customer]'] = customer.first_name
            customer_device = CustomerDevices.objects.filter(customer__id=customer.id)\
                                .order_by('-created_date').first()
            
            for key in keys_dict:
                body = body.replace(key,keys_dict[key])
                title = title.replace(key,keys_dict[key])
                
            registration_token= customer_device.device_id
            message = messaging.Message(
                notification=messaging.Notification(
                    title=title,
                    body=body,
                    ),
                    token=registration_token,
            )
            firebase_response = messaging.send(message)

            # Call Message Service API IF send message sucessfully
            # Save sent message message
            if promo_code:
                customer_notification = CustomerNotification(promo_code=promo_code,notification_template=notification_temp, customer=customer,
                                    notification_title=title, notification_body=body)
            else:
                customer_notification = CustomerNotification(notification_template=notification_temp, customer=customer,
                                    notification_title=title, notification_body=body)
            customer_notification.save()
                      
    return Response("SMS sent.", status=status.HTTP_200_OK)
