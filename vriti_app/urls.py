from django.urls import path, include
from . import views
from .views import SerialData, UsersApiView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('users', SerialData, basename = 'users')

urlpatterns = [
    # path("users", views.SerialData),
    path("users", views.UsersApiView.as_view()),
    path("user/<slug:username>", views.UserDetails.as_view()),
    # path('', include(router.urls)),
    path("", views.signUp, name = 'signUp'),
    path("home", views.home, name = 'home'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
]
