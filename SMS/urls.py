from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import SMSViewSet, SMSTemplateViewSet, CustomerSMSViewSet,\
    send_sms
router = SimpleRouter()

router.register(r'sms', SMSViewSet)
router.register(r'smstemplate', SMSTemplateViewSet)
router.register(r'customersms', CustomerSMSViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^sendsms/', send_sms, name='sendsms'),
]