from django.urls import path, include

from . import views

app_name = 'pocess'
urlpatterns = [
    path('index/', views.show_process, name='show_process'),
    # path('new/', views.new, name='new'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # path('cart/', include('cart.urls')),
    # path('chat/', include('chat.urls')),
    # path('rating/',include('rating.urls')),
    
]