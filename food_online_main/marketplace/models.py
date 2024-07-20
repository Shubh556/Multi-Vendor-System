# Importing the models module from Django to create model classes
from django.db import models

# Importing the User model from the accounts application
from accounts.models import User
# Importing the FoodItem model from the menu application
from menu.models import FoodItem


# Creating the Cart model to represent items added to a user's cart
class Cart(models.Model):
    # Defining the fields of the Cart model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each cart item is associated with a user; if the user is deleted, the cart item is also deleted
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Each cart item is associated with a food item; if the food item is deleted, the cart item is also deleted
    quantity = models.PositiveIntegerField()  # Quantity of the food item in the cart, must be a positive integer
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the cart item was created, automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update to the cart item, automatically updated

    # Method to return a string representation of the model (for older versions of Python and Django)
    def __unicode__(self):
        return self.user


# Creating the Tax model to represent different types of taxes
class Tax(models.Model):
    # Defining the fields of the Tax model
    tax_type = models.CharField(max_length=20, unique=True)  # Type of tax, must be unique and have a maximum length of 20 characters
    tax_percentage = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Tax Percentage (%)')  # Percentage of the tax, with up to 4 digits and 2 decimal places
    is_active = models.BooleanField(default=True)  # Boolean indicating whether the tax is active, defaults to True

    # Meta class to define additional properties of the model
    class Meta:
        verbose_name_plural = 'tax'  # Plural name for the model in the admin interface

    # Method to return a string representation of the model
    def __str__(self):
        return self.tax_type  # Returns the tax type as the string representation
