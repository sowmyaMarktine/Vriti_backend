from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
from .models import * 
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required


def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form':form}

        return render(request, 'sign_up.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password=password)
            if user is not None:
                user_login(request, user)
                messages.success(request,"Successfully logged in")
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
                # return render(request, 'login.html', {'result': 'login page')

        return render(request, 'login.html', {'result': 'login page'})

def logout(request):
    user_logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'result': 'home page'})
