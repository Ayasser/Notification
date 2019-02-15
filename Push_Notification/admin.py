from django.contrib import admin

from .models import Notification, NotificationTemplate, CustomerNotification
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['header', 'created_date', 'modified_date', 'created_by', 'modified_by',]
    list_filter = ['header', 'created_date', 'modified_date', 'created_by', 'modified_by',]
    search_fields = ('header', 'created_date', 'modified_date', 'created_by', 'modified_by',)


class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ['notification_title','notification_body', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'notification',]
    list_filter = ['notification_title','notification_body', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'notification',]
    search_fields = ('notification_title','notification_body', 'created_date', 'modified_date', 
                    'created_by','modified_by', 'language', 'notification',)


class CustomerNotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_template', 'customer', 'sent_date', 'promo_code', 'notification_title','notification_body', ]
    list_filter = ['notification_template', 'customer', 'sent_date', 'promo_code', 'notification_title','notification_body', ]
    search_fields = ('notification_template', 'customer', 'sent_date', 'promo_code', 'notification_title','notification_body',)

admin.site.register(Notification,NotificationAdmin)
admin.site.register(NotificationTemplate,NotificationTemplateAdmin)
admin.site.register(CustomerNotification,CustomerNotificationAdmin)
