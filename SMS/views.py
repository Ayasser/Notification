from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer.models import Customer
from Promo_code.models import PromoCode
from .models import SMS, SMSTemplate, CustomerSMS
from .serializers import SMSSerializer, SMSTemplateSerializer, \
    CustomerSMSSerializer

# Create your views here.

class SMSViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`SMS<SMS.models.SMS>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = SMS.objects.all()
    serializer_class= SMSSerializer


class SMSTemplateViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`SMSTemplate<SMS.models.SMSTemplate>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = SMSTemplate.objects.all()
    serializer_class= SMSTemplateSerializer


class CustomerSMSViewSet(viewsets.ModelViewSet):
    """
    | Default CRUD view set for :py:class:`CustomerSMS<SMS.models.CustomerSMS>`.

    * Supports Pagination: *No*
    * Search Fields: **None**
    * Ordering Fields: **None**
    * Filter Fields: **None**
    """
    queryset = CustomerSMS.objects.all()
    serializer_class= CustomerSMSSerializer

@api_view(['GET'])
def send_sms(request):
    """
    | Send SMS using to one or group of customer. 
        parameters : 
        -customer_ids: Customer
        -notification_id : Notification
        -promo_code_id : PromoCode
    """
    if request.method == 'GET':
        customer_ids = request.query_params.get('customer_ids')
        if customer_ids:
            customer_ids = customer_ids.split(",")
        sms_id = request.query_params.get('sms_id')
        promo_code_id = request.query_params.get('promo_code_id')

        if sms_id is None or customer_ids is None:
            return Response("Pleas Send sms_id and customer_ids", status=status.HTTP_404_NOT_FOUND)
        
        sms = SMS.objects.filter(id=sms_id).first()
        keys_dict = dict()
        promo_code = None
        if promo_code_id:
            promo_code = PromoCode.objects.filter(id=promo_code_id).first()
            if promo_code:
                keys_dict['[promo_code]'] = promo_code.code
        
        customers = Customer.objects.filter(id__in=customer_ids).order_by('language')
        
        if not customers or not sms:
            return Response("Cutomer or SMS not found", status=status.HTTP_404_NOT_FOUND)
        
        for customer in customers:
            sms_temp = SMSTemplate.objects.filter(sms__id=sms.id,language__id=customer.language.id).first()
            if sms_temp:
                message = sms_temp.message_template
                keys_dict['[customer]'] = customer.first_name
                
                for key in keys_dict:
                    message = message.replace(key,keys_dict[key])

                #Call Message Service API IF send message sucessfully
                # Save sent message message
                if promo_code:
                    customer_sms = CustomerSMS(sms_template=sms_temp,customer=customer,message=message,promo_code=promo_code)
                else:
                    customer_sms = CustomerSMS(sms_template=sms_temp,customer=customer,message=message)
                customer_sms.save()
              
        
    return Response("SMS sent.", status=status.HTTP_200_OK)
