from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Category

from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.

def signUp(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            catgry = form.cleaned_data.get('category')
            Category.objects.create(user=user,category=catgry)

            return redirect('login')

    return render(request, 'sign_up.html', {'result': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        print(user)
        if user is not None:
            # print("inside the condition")
            auth_login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'result': 'login page'})

def home(request):
    return render(request, 'home.html', {'result': 'Home page'})
