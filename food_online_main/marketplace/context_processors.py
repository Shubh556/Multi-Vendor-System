# Importing the Cart and Tax models from the marketplace application
from marketplace.models import Cart, Tax
# Importing the FoodItem model from the menu application
from menu.models import FoodItem


# Function to get the total number of items in the user's cart
def get_cart_counter(request):
    cart_count = 0  # Initializing the cart count to 0
    if request.user.is_authenticated:  # Checking if the user is logged in
        try:
            # Fetching all cart items for the logged-in user
            cart_items = Cart.objects.filter(user=request.user)
            if cart_items:  # If there are cart items
                for cart_item in cart_items:
                    # Adding the quantity of each cart item to the cart count
                    cart_count += cart_item.quantity
            else:
                cart_count = 0  # If there are no cart items, cart count remains 0
        except:
            cart_count = 0  # In case of an error, set cart count to 0
    # Returning the cart count as a dictionary
    return dict(cart_count=cart_count)


# Function to get the subtotal, tax, and grand total amounts for the user's cart
def get_cart_amt(request):
    subtotal = 0  # Initializing the subtotal to 0
    tax = 0  # Initializing the tax amount to 0
    grand_total = 0  # Initializing the grand total to 0
    tax_dict = {}  # Initializing an empty dictionary to store tax details
    
    if request.user.is_authenticated:  # Checking if the user is logged in
        # Fetching all cart items for the logged-in user
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            # Fetching the food item associated with each cart item
            fooditem = FoodItem.objects.get(pk=item.fooditem.id)
            # Adding the price of the food item multiplied by its quantity to the subtotal
            subtotal += (fooditem.price * item.quantity)
            
        # Fetching all active tax records
        get_tax = Tax.objects.filter(is_active=True)
        for i in get_tax:
            tax_type = i.tax_type  # Getting the type of tax
            tax_percentage = i.tax_percentage  # Getting the tax percentage
            # Calculating the tax amount based on the subtotal
            tax_amt = round((tax_percentage * subtotal) / 100, 2)
            # Updating the tax dictionary with the tax details
            tax_dict.update({tax_type: {str(tax_percentage): tax_amt}})
            
        # Calculating the total tax amount
        tax = sum(x for key in tax_dict.values() for x in key.values())
        # Calculating the grand total by adding the subtotal and tax
        grand_total = subtotal + tax
    
    # Returning the subtotal, tax, grand total, and tax details as a dictionary
    return dict(subtotal=subtotal, tax=tax, grand_total=grand_total, tax_dict=tax_dict)
