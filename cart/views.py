from django.shortcuts import render, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
# from cart.cart import Cart
from .models import Cart,CartItem
from os import path
from pathlib import Path
categories = CartItem.objects.all()
BASE_DIR = Path(__file__).resolve().parent.parent
@login_required(login_url="/users/login")
def carts(request):
    
    categories = Cart.objects.all()
    print(categories)
    return render(request, str(BASE_DIR)+r"\cart\templates\cart.html", {
       
        'categories': categories,
        
    })
@login_required(login_url="/users/login")
def items1(request):
    m=request.user
    categories = CartItem.objects.all()
    print(categories)
    return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
       
        'categories': categories,
        'm':m
        
    })

# @login_required(login_url="/users/login")
# def cart_add(request):
#     cart1=Cart(request)
#     cart = CartItem(request)
#     product = Item.objects.get(name="teddy")
#     cart.product=product
#     cart.cart=cart1
#     cart.save()
#     return redirect("home")


# @login_required(login_url="/users/login")
# def item_clear(request, id):
#     cart = Cart(request)
#     product = Item.objects.get(id=id)
#     cart.remove(product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def item_increment(request, id):
#     cart = Cart(request)
#     product = Item.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def item_decrement(request, id):
#     cart = Cart(request)
#     product = Item.objects.get(id=id)
#     cart.decrement(product=product)
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("cart_detail")


# @login_required(login_url="/users/login")
# def cart_detail(request):
#     categories = Cart.objects.all()
#     return render(request, 'cart/cart_detail.html')
from django.shortcuts import render, redirect
from .models import Cart

# def add_to_cart(request, product_id):
#     if request.method == 'POST':
#         # Get the product object based on the product_id
#         product = Item.objects.get(id=product_id)
        
#         # Check if the user already has a cart
#         if request.user.is_authenticated:
#             cart = Cart.objects.filter(user=request.user).first()
#             if not cart:
#                 cart = Cart(user=request.user)
#                 cart.save()
#         else:
#             # If the user is not authenticated, handle it as per your requirement
#             # You can use session or cookies to store the cart information
            
#         # Add the product to the cart
#         cart.products.add(product)
#         cart.save()
        
#     return redirect('cart')

@login_required(login_url="/users/login")
def remove_from_cart(request, product_id):
    if request.method == 'POST':
        # Get the product object based on the product_id
        product = Item.objects.get(id=product_id)
        
        # Get the cart for the user
        cart = Cart.objects.get(user=request.user)
        
        # Remove the product from the cart
        cart.products.remove(product)
        cart.save()
        
    return redirect('cart')
@login_required(login_url="/users/login")
def cart(request):
    # Get the cart for the user
    cart = Cart.objects.get(user=request.user)
    
    context = {
        'cart': cart
    }
    
    return render(request, 'cart.html', context)


@login_required(login_url="/users/login")
def add_to_cart(request, product_name):
    # Get the product object based on the product name
    try:
        cart2 = Cart.objects.get(user=request.user)
    except:
        cart2 = Cart()
        cart2.user=request.user
        cart2.save()
    try:
        product = Item.objects.get(name=product_name)
    
        try:
            cart1 = CartItem.objects.all()
            print(cart1)
            m=0
            for i in cart1:
                if i.cart.user==request.user and i.product==product_name:
             
                    m=1
            print(m)
            if m==0:
                cart2 = Cart.objects.get(user=request.user)
                product = Item.objects.get(name=product_name)
                cart5=CartItem()
                cart5.product=product
                cart5.product=product_name
                cart5.price_ht=product.price
                cart5.cart=cart2
                cart5.save()
                print(cart2)
                print(cart5)
                
                # cart1 = CartItem.objects.all()
                # print(cart1)

                
        except:
            cart1=CartItem()
            cart1.product=product_name
            cart1.price_ht=product.price
            cart1.cart=cart2
            cart1.save()
        categories = CartItem.objects.all()
        print(categories)
        return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
        
            'categories': categories,

        
        })
    except:
        categories = CartItem.objects.all()
        return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
        
            'categories': categories,

        
        })
    
@login_required(login_url="/users/login")
def change_quantity(request,product_name,quant):
    try:
        cart1 = CartItem.objects.get(product=product_name)
        cart1.quantity=quant
        cart1.save()
    except:
        print("item not der")
    return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
       
        'categories': categories,
        
        
    })

@login_required(login_url="/users/login")
def remove_item(request,product_name):
    
    try:
        product = Item.objects.get(name=product_name)
        cart1 = CartItem.objects.all()
        for i in cart1:
            if i.product==product_name:
                i.delete()
        
    except:
        print("afg")
    categories = CartItem.objects.all()
    return render(request, str(BASE_DIR)+r"\cart\templates\cartitems.html", {
       
        'categories': categories,
    })


