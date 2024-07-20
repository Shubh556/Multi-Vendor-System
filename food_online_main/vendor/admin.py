from django.contrib import admin
from vendor.models import Vendor

# Register your models here.

# Custom admin class to manage how the Vendor model is displayed in the admin interface
class VendorAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the Vendor model
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    # Fields that should be clickable links to the detailed view
    list_display_links = ('user', 'vendor_name')
    # Fields that can be edited directly in the list view
    list_editable = ('is_approved',)

# Register the Vendor model with the custom admin class
admin.site.register(Vendor, VendorAdmin)
