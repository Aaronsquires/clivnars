from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


# Colours of Products Model
class Colours(models.Model):
    colour = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    colourcode = models.CharField(max_length=10, default='RAL')

    def __str__(self):
        return self.colour


# Supplier of Products Model
class Supplier(models.Model):
    supplier = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier


# Main Product Model
class Product(models.Model):
    # max_length required for CharField
    code = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    colour = models.ForeignKey(Colours, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default='1')
    minquantity = models.IntegerField(default='50')
    modified = models.DateTimeField(auto_now=True)
    modifiedby = models.CharField(max_length=20)
    history = HistoricalRecords()

    def is_out_of_stock(self):
        return self.quantity <= self.minquantity

    def no_stock(self):
        return self.quantity == '0'

    def set_product_code(self):
        productcode = self.code + '-' + self.colour
        return productcode

    def has_colour(self):
        colourcode = self.colour
        testparameter = "None"
        if colourcode == "None":
            return True
        else:
            return False

    def DiscountCalc(self, x):
        Calc = (self.quantity - x)
        return Calc

    def __str__(self):
        return "{} - {}".format(self.code, self.description)


class ProductBacklog(models.Model):
    products = models.ManyToManyField(Product)
    modified = models.DateTimeField(auto_now=True)





    
