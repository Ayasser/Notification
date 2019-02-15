from django.contrib import admin
from .models import PromoCode

# Register your models here.

class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['code', ]
    list_filter = ['code',]
    search_fields = ('code',)

admin.site.register(PromoCode,PromoCodeAdmin)
