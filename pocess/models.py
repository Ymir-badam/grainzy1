
from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class timeline(models.Model):
    deliveryTo=models.ForeignKey(User, on_delete=models.CASCADE)
    item=models.CharField(max_length=100)
    designComp=models.BooleanField(default=False)
    pickedUp=models.BooleanField(default=False)
    travelling=models.BooleanField(default=False)
    deliveryDone=models.BooleanField(default=False)
    def __str__(self):
        return   " -timeline "+str(self.item) +" " + str(self.deliveryTo)
