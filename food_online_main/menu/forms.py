# Importing the forms module from Django to create form classes
from django import forms

# Importing a custom validator that ensures only images are uploaded
from accounts.validators import allow_only_images_validator

# Importing the models that the forms will be based on
from .models import Category, FoodItem


# Creating a form for the Category model
class CategoryForm(forms.ModelForm):
    # Meta class to specify which model and fields the form should use
    class Meta:
        model = Category  # The model that the form will be based on
        fields = ['category_name', 'description']  # The fields of the model to be included in the form


# Creating a form for the FoodItem model
class FoodItemForm(forms.ModelForm):
    # Defining an image field with specific attributes and validation
    image = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-light w-100'}),  # Setting the CSS class for the file input
        validators=[allow_only_images_validator]  # Adding a validator to ensure only images can be uploaded
    )
    
    # Meta class to specify which model and fields the form should use
    class Meta:
        model = FoodItem  # The model that the form will be based on
        fields = ['category', 'food_title', 'description', 'price', 'image', 'is_available']  # The fields of the model to be included in the form
