# Importing the admin module from Django to register models with the admin site
from django.contrib import admin

# Importing the Cart and Tax models
from .models import Cart, Tax

# Creating a custom admin class for the Cart model
class CartAdmin(admin.ModelAdmin):
    # list_display defines the fields to display in the admin list view for the Cart model
    list_display = ('user', 'fooditem', 'quantity', 'updated_at')


# Creating a custom admin class for the Tax model
class TaxAdmin(admin.ModelAdmin):
    # list_display defines the fields to display in the admin list view for the Tax model
    list_display = ('tax_type', 'tax_percentage', 'is_active')


# Registering the Cart model with the custom CartAdmin class
admin.site.register(Cart, CartAdmin)

# Registering the Tax model with the custom TaxAdmin class
admin.site.register(Tax, TaxAdmin)
