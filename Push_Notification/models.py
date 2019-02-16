from django.db import models

from django.contrib.auth.models import User
from Customer.models import Customer, Language
from Promo_code.models import PromoCode

# Create your models here.
class Notification(models.Model):
    """
    Stores Notification. related to :py:class:`User<User.models.User>`
    """
    header = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    objects= models.Manager()

    def __str__(self):
        return self.header 

    class Meta:
        verbose_name_plural = 'notifications'
        db_table = 'notification'


class NotificationTemplate(models.Model):
    """
    Stores NotificationTemplate. related to :py:class:`User<User.models.User>` & 
    :py:class:`Language<Customer.models.Language>` and 
    :py:class:`Notification<Push_notification.models.Notification>`
    """
    notification_title = models.TextField()
    notification_body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification,on_delete=models.CASCADE)

    objects= models.Manager()

    def __str__(self):
        return self.notification_body 

    class Meta:
        verbose_name_plural = 'notification_templates'
        db_table = 'notification_template'

class CustomerNotification(models.Model):
    """
    Stores NotificationTemplate. related to :py:class:`Language<Customer.models.Language>` and 
    :py:class:`NotificationTemplate<Push_notification.models.NotificationTemplate>`
    """
    notification_template = models.ForeignKey(NotificationTemplate, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE,  blank=True, null=True)
    notification_title = models.TextField()
    notification_body = models.TextField()

    objects= models.Manager()

    def __str__(self):
        return self.notification_title 

    class Meta:
        db_table = 'customer_notification'
