from django.db import models

# Create your models here.

class City(models.Model):
    """
    Stores City.
    """
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    objects= models.Manager()

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'cities'
        db_table = 'city'

class Language(models.Model):
    """
    Stores Language.
    """
    language = models.CharField(max_length=255)
    objects= models.Manager()
    
    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = 'languages'
        db_table = 'language'

class Customer(models.Model):
    """
    Stores Customers, related to :py:class:`Language<Customer.models.Language>`.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    
    objects= models.Manager()

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    class Meta:
        verbose_name_plural = 'customers'
        db_table = 'customer'

class CustomerDevices(models.Model):
    """
    Stores Customer Devices id, related to :py:class:`Customer<Customer.models.Customer>`.
    """
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    device_id = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    objects= models.Manager()

    def __str__(self):
        return self.device_id

    class Meta:
        verbose_name_plural = 'customer_devices'
        db_table = 'customer_device'
