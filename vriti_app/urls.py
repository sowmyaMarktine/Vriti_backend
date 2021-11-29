from django.urls import path, include
from .models import User
from . import views
from .views import (
    RegistrationView,
    SerialData,
)
# from .views import UsersApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', SerialData)
# router.register('register/', RegistrationView.as_view(), basename = 'register')

# app_name = 'User'

urlpatterns = [
    # path("users", views.SerialData),
    # path("users", views.UsersApiView.as_view()),
    # path("user/<slug:username>", views.UserDetails.as_view()),
    path('', include(router.urls)),
    # path('users', SerialData.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', RegistrationView.as_view()),
    # path("", views.signUp, name = 'signUp'),
    # path("home", views.home, name = 'home'),
    # path('login', views.login, name = 'login'),
    # path('logout', views.logout, name = 'logout'),
]

# urlpatterns += router.urls
