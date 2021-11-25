from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from .models import Category
# Create your views here.
from .models import * 
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .serializers import Userserializers

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# class SerialData(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = Userserializers
    # return JsonResponse(serializers.data, safe = False)

class UsersApiView(APIView):
    parser_classes = [JSONParser]

    def get(self, request):
        queryset = User.objects.all()
        serializer_class = Userserializers(queryset, many = True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = Userserializers(data = request.data)

        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):

    def get_object(self, username):
        try:
            return User.objects.get(username = username)
        except User.DoesNotExist:
            return Response

    def get(self, request, username):
        user = self.get_object(username)
        serializer = Userserializers(user)
        return Response(serializer.data)

    def put(self, request, username):
        try:
            user = self.get_object(username)
            serializer = Userserializers(user, data = request.data)
        except:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def SerialData(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer_class = Userserializers(queryset, many = True)
        return Response(serializer_class.data)

    elif request.method == 'POST':
        serializer = Userserializers(data = request.data)

        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                catgry = form.cleaned_data.get('category')
                Category.objects.create(user=user,category=catgry)

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

@login_required(login_url='login')
def logout(request):
    user_logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'result': 'home page'})
