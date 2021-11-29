from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# admin.site.register(Category)
class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'category', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'first_name', 'last_name', 'is_active')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
