from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('options/', views.get_all_options, name='options'),
    path('options/train/', views.get_train, name='train'),
    path('options/parking/', views.get_parking, name='parking'),
    path('options/bicycle/', views.get_bicycle, name='bicycle'),
    path('options/bus/', views.get_bus, name='bus'),
    path('train_payment/', views.train_payment, name='train_payment'),
    path('parking_payment/', views.parking_payment, name='parking_payment'),
    path('bicycle_payment/', views.bicycle_payment, name='bicycle_payment'),
    path('bus_payments/', views.bus_payment, name='bus_payments'),
]