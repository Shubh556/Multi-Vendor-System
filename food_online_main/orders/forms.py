from django import forms  # Import Django's forms module
from .models import Order  # Import the Order model from the current app's models

# Define a form class for creating and updating Order instances
class OrderForm(forms.ModelForm):
    # Meta class to specify which model and fields to use
    class Meta:
        model = Order  # Specify that this form is for the Order model
        # List of fields from the Order model that will be included in the form
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'city', 'state', 'pin_code']
