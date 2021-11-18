from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Category

# Create your views here.

def home(request):
    return render(request, 'home.html', {'result': 'Home page'})

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
    return render(request, 'login.html', {'result': 'login page'})
