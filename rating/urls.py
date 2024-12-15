from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('add/<str:product_name>/<int:rating>/<str:product_review>', views.add_review, name='addRev'),
    path('show/<str:key>/', views.product_reviews, name='new'),
   
    # path('<int:pk>/', view # path('check', views.checking),s.detail, name='detail'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
]
