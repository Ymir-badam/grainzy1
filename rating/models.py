from django.db import models
from item.models import Item
from django.contrib.auth.models import User
# Create your models here.
# class rate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Item, on_delete=models.CASCADE,unique=True)
#     rating = models.IntegerField(default=5)
#     review = models.CharField(max_length=255,blank=True)
#     def __str__(self):
#         return   "Review of " + str(self.product) +" by "+str(self.user)
from django.db import models
from django.contrib.auth.models import User

# class Item(models.Model):
#     # Your existing fields for the Item model

#     def calculate_average_rating(self):
#         ratings = self.ratings.all()
#         if ratings:
#             total_ratings = len(ratings)
#             sum_ratings = sum(rating.rating_value for rating in ratings)
#             average_rating = sum_ratings / total_ratings
#             self.average_rating = average_rating
#             self.save()

#     def __str__(self):
#         return self.name

class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=255,blank=True)
    rating_value = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.item.name}: {self.rating_value}"
