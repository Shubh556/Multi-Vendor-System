from django.contrib import admin
from .models import Order, OrderedFood
from django.db.models import Sum

# Admin class for managing OrderedFood entries in the admin interface
class OrderFoodAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('customer_name', 'user', 'food_item', 'quantity', 'amount', 'order_number', 'order_total')

    # Method to display the customer's name
    def customer_name(self, obj):
        return obj.order.first_name
    
    # Method to display the food item name
    def food_item(self, obj):
        return obj.fooditem

    # Method to display the order number
    def order_number(self, obj):
        return obj.order.order_number

    # Method to display the total amount for the order
    def order_total(self, obj):
        # Get the order number
        order_number = obj.order.order_number
        # If the total for this order hasn't been calculated yet, do it now
        if order_number not in self._order_totals:
            total_amount = sum(item.amount for item in OrderedFood.objects.filter(order=obj.order))
            self._order_totals[order_number] = total_amount
        
        # Return the total amount for this order
        return self._order_totals.get(order_number)

    # Customize the queryset to initialize the _order_totals dictionary
    def get_queryset(self, request):
        # Initialize the dictionary to store totals for each order
        self._order_totals = {}
        return super().get_queryset(request)

    # Set custom column headers
    customer_name.short_description = 'Customer'
    order_total.short_description = 'Total'

# Admin class for managing Order entries in the admin interface
class OrderAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('order_number', 'first_name', 'last_name', 'phone', 'email', 'order_placed_to')

# Register the models and their admin classes with the admin site
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedFood, OrderFoodAdmin)
