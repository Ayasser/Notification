from django.contrib import admin
from .models import SMS, SMSTemplate, CustomerSMS
# Register your models here.

class SMSAdmin(admin.ModelAdmin):
    list_display = ['header', 'created_date', 'modified_date', 'created_by', 'modified_by',]
    list_filter = ['header', 'created_date', 'modified_date', 'created_by', 'modified_by',]
    search_fields = ('header', 'created_date', 'modified_date', 'created_by', 'modified_by',)


class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ['message_template', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'sms',]
    list_filter = ['message_template', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'sms',]
    search_fields = ('message_template', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'sms',)


class CustomerSMSAdmin(admin.ModelAdmin):
    list_display = ['sms_template', 'customer', 'sent_date', 'promo_code', 'message',]
    list_filter = ['sms_template', 'customer', 'sent_date', 'promo_code', 'message',]
    search_fields = ('sms_template', 'customer', 'sent_date', 'promo_code', 'message',)

admin.site.register(SMS,SMSAdmin)
admin.site.register(SMSTemplate,SMSTemplateAdmin)
admin.site.register(CustomerSMS,CustomerSMSAdmin)
