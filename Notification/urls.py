"""Notification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Notification API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^apidoc', schema_view),
    url(r'^docs/', include_docs_urls(title='API Doc')),
    url(r'', include(('Customer.urls','Customer'), namespace='Customer')),
    url(r'', include(('Promo_code.urls','Promo_code'), namespace='Promo_code')),
    url(r'', include(('Push_Notification.urls','Push_Notification'), namespace='Push_Notification')),
    url(r'', include(('SMS.urls','SMS'), namespace='SMS')),
]
