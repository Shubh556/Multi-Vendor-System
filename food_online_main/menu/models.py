# Importing the models module from Django to create model classes
from django.db import models

# Importing the Vendor model from the vendor application
from vendor.models import Vendor


# Creating the Category model to represent food categories
class Category(models.Model):
    # Defining the fields of the Category model
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Each category is associated with a vendor; if the vendor is deleted, the category is also deleted
    category_name = models.CharField(max_length=50)  # Name of the category with a maximum length of 50 characters
    slug = models.SlugField(max_length=100, unique=True)  # A unique slug for the category, used in URLs
    description = models.TextField(max_length=250, blank=True)  # A description of the category, which can be left blank
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the category was created, automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update to the category, automatically updated

    # Meta class to define additional properties of the model
    class Meta:
        verbose_name = 'category'  # Singular name for the model
        verbose_name_plural = 'categories'  # Plural name for the model

    # Method to clean the data before saving
    def clean(self):
        self.category_name = self.category_name.capitalize()  # Capitalizes the category name before saving

    # Method to return a string representation of the model
    def __str__(self):
        return self.category_name  # Returns the category name as the string representation


# Creating the FoodItem model to represent individual food items
class FoodItem(models.Model):
    # Defining the fields of the FoodItem model
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # Each food item is associated with a vendor; if the vendor is deleted, the food item is also deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fooditems')  # Each food item belongs to a category; if the category is deleted, the food item is also deleted
    food_title = models.CharField(max_length=50)  # Title of the food item with a maximum length of 50 characters
    slug = models.SlugField(max_length=100, unique=True)  # A unique slug for the food item, used in URLs
    description = models.TextField(max_length=250, blank=True)  # A description of the food item, which can be left blank
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the food item with a maximum of 10 digits and 2 decimal places
    image = models.ImageField(upload_to='foodimages')  # Image of the food item, uploaded to the 'foodimages' directory
    is_available = models.BooleanField(default=True)  # A boolean indicating whether the food item is available, default is True
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the food item was created, automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update to the food item, automatically updated

    # Method to return a string representation of the model
    def __str__(self):
        return self.food_title  # Returns the food title as the string representation
