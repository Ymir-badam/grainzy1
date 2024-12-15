from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })
@login_required
def user_logout(request):
    auth.logout(request)
    # return redirect('dashboard/logout')
    return redirect("/login")
