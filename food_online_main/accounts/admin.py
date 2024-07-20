from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Define a custom admin class for the User model
class CustomUserAdmin(UserAdmin):
    # These fields will be displayed as columns in the list view of the admin interface
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    
    # Orders the users by the date they joined in descending order (newest first)
    ordering = ('-date_joined',)
    
    # These settings disable some default configurations for the admin interface
    filter_horizontal = ()  # Disables horizontal filtering (not needed here)
    list_filter = ()  # Disables filtering options in the admin interface
    fieldsets = ()  # Disables field grouping in the admin interface

# Register the User model with the custom admin class
admin.site.register(User, CustomUserAdmin)

# Register the UserProfile model with the default admin interface
admin.site.register(UserProfile)
