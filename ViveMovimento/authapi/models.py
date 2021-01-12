from django.db import models
import uuid
# Create your models here.
class food_journal(models.Model):
    foodname = (
        ('Pollo Cocido', 'Pollo Cocido'),
        ('Arroz Cocido', 'Arroz Cocido'),
        ('Spaghetti Carbonara', 'Spaghetti Carbonara'),
    )
    foodmacro = (
        ('Proteina', 'Proteina'),
        ('Carbohidratos', 'Carbohidratos'),
    )
    food_name = models.CharField(max_length=200, null = False, choices = foodname)
    food_portion_quantity = models.IntegerField(null = False)
    food_macro = models.CharField(max_length=200, null = False, choices = foodmacro)
    food_serving_quantity = models.IntegerField(null = False)
    macro_total = models.IntegerField(null = True, blank = True)
    uuid = models.IntegerField(null = False)

    def save(self, *args, **kwargs):
        self.macro_total = self.food_portion_quantity * self.food_serving_quantity
        
        super().save(*args, **kwargs)

    