from django import forms
from .models import User, UserProfile  # Import the User and UserProfile models
from .validators import allow_only_images_validator  # Import a custom validator for images

# Define a form for creating and updating User objects
class UserForm(forms.ModelForm):
    # Define password fields with password input widgets (to mask the input)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User  # Specify the model this form is for
        fields = ['first_name', 'last_name', 'username', 'email', 'password']  # Specify the fields to include in the form

    # Define a clean method to add custom validation logic
    def clean(self):
        cleaned_data = super(UserForm, self).clean()  # Call the parent class's clean method
        password = cleaned_data.get('password')  # Get the password from the cleaned data
        confirm_password = cleaned_data.get('confirm_password')  # Get the confirm_password from the cleaned data

        if password != confirm_password:  # Check if passwords match
            raise forms.ValidationError("Password does not match!")  # Raise a validation error if they don't

# Define a form for creating and updating UserProfile objects
class UserProfileForm(forms.ModelForm):
    # Define fields with specific widgets and attributes
    address = forms.CharField(widget=forms.TextInput(attrs={'required': 'required'}))
    profile_picture = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-light'}), 
        validators=[allow_only_images_validator]  # Use custom validator to allow only images
    )
    cover_photo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-light'}), 
        validators=[allow_only_images_validator]  # Use custom validator to allow only images
    )
    
    class Meta:
        model = UserProfile  # Specify the model this form is for
        fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code']  # Specify the fields to include in the form

# Define a form for updating basic user information
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User  # Specify the model this form is for
        fields = ['first_name', 'last_name', 'phone_number']  # Specify the fields to include in the form
