from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import PromoCodeViewSet
router = SimpleRouter()

router.register(r'promocode', PromoCodeViewSet)

urlpatterns = [
    url('', include(router.urls)),
]