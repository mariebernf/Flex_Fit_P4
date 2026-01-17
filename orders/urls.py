from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<str:order_number>/', views.checkout_success, name='checkout_success'),
    path('history/', views.order_history, name='order_history'),
]
