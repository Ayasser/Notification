from django.db import models

# Create your models here.

class PromoCode(models.Model):
    """
    Stores PromoCode.
    """
    code = models.CharField(max_length=50)
    objects= models.Manager()
    
    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Promocodes'
        db_table = 'promocode'
