from django.contrib import admin
from .models import City, Language, Customer, CustomerDevices
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = [ 'name_en','name_ar']
    list_filter = ['name_en','name_ar']
    search_fields = ('name_en','name_ar')

admin.site.register(City,CityAdmin)
