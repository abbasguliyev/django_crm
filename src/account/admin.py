from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.

@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'is_superuser', 'is_active'
    )
    list_display_links = ('id', 'email')
