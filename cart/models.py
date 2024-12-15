from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from item.models import Item

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    # products = models.ManyToManyField(Item)
    name=str(user)+" cart"
    
    def __str__(self):
        return   " -cart " + str(self.user)
    

class CartItem(models.Model):
    # product = models.ForeignKey(Item, on_delete=models.CASCADE,unique=True)
    product=models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht * (1 + self.TAX_AMOUNT/100.0)

    def __str__(self):
        return  str(self.cart.user)+ " - " + str(self.product)
