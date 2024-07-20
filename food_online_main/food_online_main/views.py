from django.shortcuts import render
from django.http import HttpResponse
from vendor.models import Vendor

def home(request):
    # Fetch vendors who are approved and their user account is active
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    print(vendors)  # Print the list of vendors to the console (for debugging purposes)

    # Prepare the context dictionary to pass to the template
    context = {
        'vendors': vendors,  # Pass the list of approved and active vendors
    }

    # Render the 'home.html' template with the context data
    return render(request, 'home.html', context)
