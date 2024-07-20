from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserProfileForm, UserInfoForm
from django.contrib import messages
from accounts.models import UserProfile
from orders.models import Order, OrderedFood
import simplejson as json

# Ensure that only logged-in users can access this view
@login_required(login_url='login')
def cprofile(request):
    # Get the UserProfile object for the currently logged-in user
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # If the request method is POST, handle form submission
    if request.method == 'POST':
        # Create form instances with the submitted data
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserInfoForm(request.POST, request.FILES, instance=request.user)
        
        # Check if both forms are valid
        if profile_form.is_valid() and user_form.is_valid():
            # Save the forms and display a success message
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile Updated')
            return redirect('cprofile')
        else:
            # Print form errors if any
            print(profile_form.errors)
            print(user_form.errors)
    else:
        # If the request method is GET, create form instances with initial data
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)
    
    # Pass the forms and profile to the template
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request, 'customers/cprofile.html', context)

# Display the user's orders
@login_required(login_url='login')
def my_orders(request):
    # Get the list of orders for the currently logged-in user, sorted by creation date
    orders = Order.objects.filter(user=request.user).order_by('created_at')
    
    # Pass the orders to the template
    context = {
        'orders': orders,
    }
    return render(request, 'customers/my_orders.html', context)

# Display the details of a specific order
@login_required(login_url='login')
def order_detail(request, order_number):
    # Get the specific order by its order number and the logged-in user
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    
    # Get the food items associated with this order
    ordered_food_items = OrderedFood.objects.filter(order=order)
    
    # Calculate the subtotal for the order
    subtotal = 0
    for item in ordered_food_items:
        subtotal += (item.price * item.quantity)
    
    # Pass the order details, food items, and subtotal to the template
    context = {
        'order': order,
        'ordered_food_items': ordered_food_items,
        'subtotal': subtotal,
    }
    return render(request, 'customers/order_detail.html', context)
