from django.contrib import admin
from .models import Category, FoodItem

# Define how the Category model will be displayed in the admin interface
class CategoryAdmin(admin.ModelAdmin):
    # Automatically fill the 'slug' field based on the 'category_name' field
    prepopulated_fields = {'slug': ('category_name',)}

    # Specify which fields to display in the list view
    list_display = ('category_name', 'vendor', 'updated_at')

    # Add a search box for the specified fields
    search_fields = ('category_name', 'vendor__vendor_name')


# Define how the FoodItem model will be displayed in the admin interface
class FoodItemAdmin(admin.ModelAdmin):
    # Automatically fill the 'slug' field based on the 'food_title' field
    prepopulated_fields = {'slug': ('food_title',)}

    # Specify which fields to display in the list view
    list_display = ('food_title', 'category', 'vendor', 'price', 'is_available', 'updated_at')

    # Add a search box for the specified fields
    search_fields = ('food_title', 'category__category_name', 'vendor__vendor_name', 'price')

    # Add filters in the list view for the specified fields
    list_filter = ('is_available',)


# Register the Category model with the CategoryAdmin options
admin.site.register(Category, CategoryAdmin)

# Register the FoodItem model with the FoodItemAdmin options
admin.site.register(FoodItem, FoodItemAdmin)
