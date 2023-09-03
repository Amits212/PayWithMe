from django.shortcuts import render
from .models import TBpayment

def login(request):
    return render(request, 'login.html')

def get_all_options(request):
    return render(request, 'options.html')

def get_train(request):
    return render(request, 'train.html')

def train_payment(request):
    return render(request, 'train_payment.html')

def get_parking(request):
    return render(request, 'parking.html')

def parking_payment(request):
    return render(request, 'parking_payment.html')

def get_bicycle(request):
    return render(request, 'bicycle.html')

def bicycle_payment(request):
    return render(request, 'bicycle_payment.html')

def get_bus(request):
    return render(request, 'bus.html')

def bus_payment(request):
    return render(request, 'bus_payments.html')




