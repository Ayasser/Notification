from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import CityViewSet, LanguageViewSet, CustomerDevicesViewSet ,CustomerViewSet
router = SimpleRouter()

router.register(r'city', CityViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customerdevices', CustomerDevicesViewSet)

urlpatterns = [
    url('', include(router.urls)),
]