from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer.models import Customer
from Promo_code.models import PromoCode
from .models import Notification, NotificationTemplate, CustomerNotification
# Create your views here.

@api_view(['GET'])
def sendSMS(request):
    if request.method == 'GET':
        customer_ids = request.query_params.get('customer_ids')
        if customer_ids:
            customer_ids = customer_ids.split(",")
        notification_id = request.query_params.get('notification_id')
        promo_code_id = request.query_params.get('promo_code_id')
        
        if notification_id is None or customer_ids is None:
            return Response("ERORR", status=status.HTTP_404_NOT_FOUND)
        
        notification = Notification.objects.filter(id=notification)
        keys_dict = dict()

        if promo_code_id:
            promo_code = PromoCode.objects.filter(id=promo_code_id)
            if promo_code:
                keys_dict['[promo_code]'] = promo_code.code
        
        customers = Customer.objects.filter(id__in=customer_ids).order_by('-language')
        
        if not customers or not notification:
            return Response("ERORR", status=status.HTTP_404_NOT_FOUND)

        for customer in customers:
            notification_temp = NotificationTemplate.objects.filter(notification=notification.id,
                language__id=customer.language.id)
            title = notification_temp.title
            body = notification_temp.body
            
            keys_dict['[customer]'] = customer.first_name
            
            for key in keys_dict:
                title = title.replace(key,keys_dict[key])
                body = body.replace(key,keys_dict[key])
            #send message
            #

                
                
        
    return Response("notification is sent.", status=400)
