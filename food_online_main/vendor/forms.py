from django import forms
from .models import Vendor
from accounts.validators import allow_only_images_validator

# Define a form for the Vendor model
class VendorForm(forms.ModelForm):
    # Add a file input field for the vendor's license with custom styling and validation
    vendor_license = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-light'}),  # Apply CSS class to the file input field
        validators=[allow_only_images_validator]  # Apply custom validator to ensure only images are uploaded
    )

    class Meta:
        model = Vendor  # Specify the model this form is associated with
        fields = ['vendor_name', 'vendor_license']  # Specify the fields to include in the form
