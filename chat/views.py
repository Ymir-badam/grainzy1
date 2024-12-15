from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
from chat.models import Thread


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    print(threads)
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)
@login_required
def create_thread(request,id):
    
    
    User = get_user_model()
    users = User.objects.all()
    print(users) 
    try:
        for i in users:
            if i.get_username()==id:
                thread=Thread()
                thread.first_person=request.user
                thread.second_person=i
                thread.save()
    except:
        print("badam")
    
    return render(request, 'hello.html')
