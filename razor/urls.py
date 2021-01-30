from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_page, name='paymment_page'),
    path('success', views.success, name='payment_status'),
]
