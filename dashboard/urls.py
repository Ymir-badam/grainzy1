from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/',views.user_logout,name="user-logout"),
    path('dashboard/logout/',views.user_logout,name="user-logout"),
]
