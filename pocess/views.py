from django.shortcuts import render
from .models import timeline
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def show_process(request):
    t=timeline.objects.all()
    
    # pass