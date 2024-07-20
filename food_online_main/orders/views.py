from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from marketplace.models import Cart, FoodItem
from .models import Order, OrderedFood
from .forms import OrderForm
import simplejson as json
from .utils import generate_order_number
from marketplace.context_processors import get_cart_amt
from accounts.utils import send_notification
from django.contrib.sites.shortcuts import get_current_site

# Ensure the user is logged in to access this view
@login_required(login_url='login')
def place_order(request):
    # Get all items in the user's cart, ordered by creation date
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    cart_count = cart_items.count()
    # If the cart is empty, redirect to the marketplace
    if cart_count <= 0:
        return redirect('marketplace')

    vendor_ids = []
    # Collect unique vendor IDs from the cart items
    for item in cart_items:
        if item.fooditem.vendor.id not in vendor_ids:
            vendor_ids.append(item.fooditem.vendor.id)
    print(vendor_ids)

    # Get the cart amount details
    subtotal = get_cart_amt(request)['subtotal']
    total_tax = get_cart_amt(request)['tax']
    grand_total = get_cart_amt(request)['grand_total']
    tax_data = get_cart_amt(request)['tax_dict']

    # If the form is submitted via POST request
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Create a new order instance with form data
            order = Order()
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.state = form.cleaned_data['state']
            order.pin_code = form.cleaned_data['pin_code']
            order.city = form.cleaned_data['city']
            order.user = request.user
            order.total = grand_total
            order.tax_data = json.dumps(tax_data)
            order.total_tax = total_tax
            order.save()
            order.order_number = generate_order_number(order.id)
            order.vendors.add(*vendor_ids)
            order.save()

            # Create ordered food items for each item in the cart
            for item in cart_items:
                ordered_food = OrderedFood(
                    order=order,
                    user=request.user,
                    fooditem=item.fooditem,
                    quantity=item.quantity,
                    price=item.fooditem.price,
                    amount=item.fooditem.price * item.quantity
                )
                ordered_food.save()

            # Send order confirmation email to the customer
            mail_subject = 'Thank You For Ordering'
            mail_template = 'orders/order_confirmation_email.html'
            ordered_food = OrderedFood.objects.filter(order=order)
            context = {
                'user': request.user,
                'order': order,
                'to_email': order.email,
                'ordered_food': ordered_food,
                'domain': get_current_site(request),
            }
            send_notification(mail_subject, mail_template, context)

            # Send new order notification email to the vendors
            mail_subject = 'You have received a new order'
            mail_template = 'orders/new_order_received.html'
            to_emails = []
            for item in cart_items:
                if item.fooditem.vendor.user.email not in to_emails:
                    to_emails.append(item.fooditem.vendor.user.email)
                    ordered_food_to_vendor = OrderedFood.objects.filter(order=order, fooditem__vendor=item.fooditem.vendor)
            context = {
                'order': order,
                'to_email': to_emails,
                'ordered_food_to_vendor': ordered_food_to_vendor,
            }
            send_notification(mail_subject, mail_template, context)

            # Clear the cart after saving the order
            cart_items.delete()

            # Redirect to order confirmation page
            return redirect('order_confirmation', order_number=order.order_number)
        else:
            print(form.errors)

    # If the request is not POST, show the order placement page
    order = Order.objects.filter(user=request.user).last()
    ordered_food_items = OrderedFood.objects.filter(order=order)

    context = {
        'order': order,
        'cart_items': cart_items,
        'ordered_food_items': ordered_food_items,
    }
    return render(request, 'orders/place_order.html', context)

# Order confirmation view
def order_confirmation(request, order_number):
    try:
        # Get the order by order number
        order = Order.objects.get(order_number=order_number)
        ordered_food = OrderedFood.objects.filter(order=order)

        # Calculate the subtotal
        subtotal = 0
        for item in ordered_food:
            subtotal += (item.price * item.quantity)

        # Load the tax data from JSON
        tax_data = json.loads(order.tax_data)
        context = {
            'order': order,
            'ordered_food': ordered_food,
            'subtotal': subtotal,
            'tax_data': tax_data,
        }
        return render(request, 'orders/order_confirmation.html', context)
    except:
        # If the order is not found, redirect to home page
        return redirect('home')
