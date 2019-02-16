from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import NotificationViewSet, NotificationTemplateViewSet, CustomerNotificationViewSet,\
    send_notification
router = SimpleRouter()

router.register(r'notification', NotificationViewSet)
router.register(r'notificationtemplate', NotificationTemplateViewSet)
router.register(r'customernotification', CustomerNotificationViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^sendnotification/', send_notification),
]