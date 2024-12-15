from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page,name="inbox1"),
    path('bad/<str:id>/', views.create_thread,name="create_chat"),
]
