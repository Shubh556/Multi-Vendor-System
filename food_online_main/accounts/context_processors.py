from urllib.parse import uses_relative
from accounts.models import UserProfile
from vendor.models import Vendor
from django.conf import settings

# Function to get the vendor associated with the current user making the request
def get_vendor(request):
    try:
        # Attempt to retrieve the Vendor object associated with the user making the request
        vendor = Vendor.objects.get(user=request.user)
    except:
        # If no Vendor object is found or an error occurs, set vendor to None
        vendor = None
    # Return the vendor object in a dictionary
    return dict(vendor=vendor)

# Function to get the user profile associated with the current user making the request
def get_user_profile(request):
    try:
        # Attempt to retrieve the UserProfile object associated with the user making the request
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        # If no UserProfile object is found or an error occurs, set user_profile to None
        user_profile = None
    # Return the user_profile object in a dictionary
    return dict(user_profile=user_profile)
