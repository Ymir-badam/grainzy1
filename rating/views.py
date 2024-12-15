from django.shortcuts import render
from .models import Rating
from django.contrib.auth.decorators import login_required
from item.models import Item

# Create your views here.
from cart.models import Cart,CartItem
from os import path
from pathlib import Path
categories = CartItem.objects.all()
BASE_DIR = Path(__file__).resolve().parent.parent
@login_required(login_url="/users/login")
def add_review(request, product_name,rating,product_review):
        rate2=Rating.objects.all()
        product = Item.objects.get(name=product_name)
        try:
                 for i in rate2:
                         if i.item==product:
                                 i.rating_value=rating
                                 i.review=product_review
                                 i.save()
                                 
        except:

                rate1=Rating()
                rate1.item=product
                rate1.user=request.user
                rate1.rating_value=rating
                rate1.review=product_review
                rate1.save()
        categories = CartItem.objects.all()
        return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
        
            'categories': categories,

        
        })
# @login_required(login_url="/users/login")
# def checking(request):
#         print(request.user.email)
@login_required(login_url="/users/login")
def product_reviews(request, product_name):
        rate1=Rating.objects.all()
        product = Item.objects.get(name=product_name)
        rate_avg=0
        rate_num=0
        for i in rate1:
                if i.item==product:
                        rate_avg+=i.rating_value
                        rate_num+=1
        if rate_num==0:
                print("no ratings")
        else:
                print(rate_avg/rate_num)
                
        categories = CartItem.objects.all()
        return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
        
            'categories': categories,

        
        })
