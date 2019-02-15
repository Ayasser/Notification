from django.db import models
from django.contrib.auth.models import User
from Customer.models import Customer, Language
from Promo_code.models import PromoCode

# Create your models here.

class SMS(models.Model):
    header = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    objects= models.Manager()

    def __str__(self):
        return self.header 

    class Meta:
        verbose_name_plural = 'sms'
        db_table = 'sms'


class SMSTemplate(models.Model):
    message_template = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    sms = models.ForeignKey(SMS,on_delete=models.CASCADE)

    objects= models.Manager()

    def __str__(self):
        return self.message_template 

    class Meta:
        verbose_name_plural = 'sms_templates'
        db_table = 'sms_template'

class CustomerSMS(models.Model):
    sms_template = models.ForeignKey(SMSTemplate, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE,  blank=True, null=True)
    message = models.TextField()

    objects= models.Manager()

    def __str__(self):
        return self.message 

    class Meta:
        db_table = 'customer_sms'
