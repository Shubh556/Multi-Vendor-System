# Import necessary modules and functions
from django.http import HttpResponse, JsonResponse  # For handling HTTP responses
from django.shortcuts import render, get_object_or_404, redirect  # For rendering templates and handling objects
from accounts.models import UserProfile  # Importing UserProfile model
from menu.models import Category, FoodItem  # Importing Category and FoodItem models
from vendor.models import Vendor  # Importing Vendor model
from django.db.models import Prefetch, Q  # For optimizing queries
from marketplace.models import Cart  # Importing Cart model
from marketplace.context_processors import get_cart_counter, get_cart_amt  # Importing custom context processors
from django.contrib.auth.decorators import login_required, user_passes_test  # For authentication and permission checks
from orders.forms import OrderForm  # Importing OrderForm for checkout
from accounts.views import check_role_customer  # Importing custom user role check

# View function for the marketplace homepage
def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)  # Fetch approved and active vendors
    vendor_count = vendors.count()  # Count the number of vendors
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html', context)  # Render the marketplace listings page with context

# View function for vendor detail page
def vendor_detail(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)  # Fetch vendor based on slug or return 404
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset=FoodItem.objects.filter(is_available=True)
        )
    )
    cart_items = Cart.objects.filter(user=request.user) if request.user.is_authenticated else None
    context = {
        'vendor': vendor,
        'categories': categories,
        'cart_items': cart_items,
    }
    return render(request, 'marketplace/vendor_detail.html', context)  # Render vendor detail page with context

# View function to add a food item to the cart
def add_to_cart(request, food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
            try:
                fooditem = FoodItem.objects.get(id=food_id)  # Check if the food item exists
                try:
                    chkCart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    chkCart.quantity += 1  # Increase the cart quantity
                    chkCart.save()
                    return JsonResponse({'status': 'Success', 'message': 'Increased the cart quantity', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amt(request)})
                except:
                    chkCart = Cart.objects.create(user=request.user, fooditem=fooditem, quantity=1)
                    return JsonResponse({'status': 'Success', 'message': 'Added the food to the cart', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amt(request)})
            except:
                return JsonResponse({'status': 'Failed', 'message': 'This food does not exist!'})
        else:
            return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})
    else:
        return JsonResponse({'status': 'login_required', 'message': 'Please login to continue'})

# View function to decrease the quantity of a food item in the cart
def decrease_cart(request, food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
            try:
                fooditem = FoodItem.objects.get(id=food_id)  # Check if the food item exists
                try:
                    chkCart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    if chkCart.quantity > 1:
                        chkCart.quantity -= 1  # Decrease the cart quantity
                        chkCart.save()
                    else:
                        chkCart.delete()
                        chkCart.quantity = 0
                    return JsonResponse({'status': 'Success', 'cart_counter': get_cart_counter(request), 'qty': chkCart.quantity, 'cart_amount': get_cart_amt(request)})
                except:
                    return JsonResponse({'status': 'Failed', 'message': 'You do not have this item in your cart!'})
            except:
                return JsonResponse({'status': 'Failed', 'message': 'This food does not exist!'})
        else:
            return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})
    else:
        return JsonResponse({'status': 'login_required', 'message': 'Please login to continue'})

# View function for the cart page, requires login
@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')  # Fetch cart items for the user
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'marketplace/cart.html', context)  # Render the cart page with context

# View function to delete a cart item
def delete_cart(request, cart_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
            try:
                cart_item = get_object_or_404(Cart, user=request.user, id=cart_id)  # Fetch cart item or return 404
                cart_item.delete()  # Delete the cart item
                return JsonResponse({'status': 'Success', 'message': 'Cart Item Deleted', 'cart_counter': get_cart_counter(request), 'cart_amount': get_cart_amt(request)})
            except Cart.DoesNotExist:
                return JsonResponse({'status': 'Failed', 'message': 'Cart Item does not exist!'})
        else:
            return JsonResponse({'status': 'Failed', 'message': 'Invalid request!'})
    else:
        return JsonResponse({'status': 'Failed', 'message': 'User not authenticated!'})

# View function to search for vendors and food items
def search(request):
    keyword = request.GET['keyword']
    fetch_vendors_by_fooditems = FoodItem.objects.filter(food_title__icontains=keyword, is_available=True).values_list('vendor', flat=True)
    vendors = Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword, is_approved=True, user__is_active=True))
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html', context)  # Render the search results page with context

# View function for the checkout page, requires login and customer role
@login_required(login_url='login')
@user_passes_test(check_role_customer)
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')  # Fetch cart items for the user
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('marketplace')  # Redirect to marketplace if cart is empty
    user_profile = UserProfile.objects.get(user=request.user)  # Fetch user profile
    default_values = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phone': request.user.phone_number,
        'email': request.user.email,
        'address': user_profile.address,
        'state': user_profile.state,
        'city': user_profile.city,
        'pin_code': user_profile.pin_code,
    }
    form = OrderForm(initial=default_values)  # Pre-fill order form with default values
    context = {
        'form': form,
        'cart_items': cart_items,
    }
    return render(request, 'marketplace/checkout.html', context)  # Render the checkout page with context
