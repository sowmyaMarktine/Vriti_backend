from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'result': 'home page'})

def signUp(request):
    return render(request, 'sign_up.html', {'result': 'sign up page'})

def login(request):
    return render(request, 'login.html', {'result': 'login page'})
