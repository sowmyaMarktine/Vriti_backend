from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# admin.site.register(Category)
class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'firstname', 'lastname', 'is_staff')
    search_fields = ('email', 'username'),
    # readonly_fields = ('id', 'firstname', 'lastname', 'is_staff')

admin.site.register(User)
