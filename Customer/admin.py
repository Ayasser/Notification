from django.contrib import admin
from .models import City, Language, Customer, CustomerDevices
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = [ 'name_en','name_ar']
    list_filter = ['name_en','name_ar']
    search_fields = ('name_en','name_ar')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language']
    list_filter = ['language']
    search_fields = ('language',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','birth_date','phone_number',
                'email','city','language',]
    list_filter = [ 'first_name','last_name','birth_date','phone_number',
                'email','city','language',]
    search_fields = ( 'first_name','last_name','birth_date','phone_number',
                'email','city','language',)


class CustomerDevicesAdmin(admin.ModelAdmin):
    list_display = ['customer','device_id','created_date',]
    list_filter = ['customer','device_id','created_date',]
    search_fields = ('customer','device_id','created_date',)

admin.site.register(City,CityAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(CustomerDevices,CustomerDevicesAdmin)
