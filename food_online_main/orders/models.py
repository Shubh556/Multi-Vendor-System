import json  # Import the JSON module
from django.db import models  # Import Django's models module
from accounts.models import User  # Import the User model
from menu.models import FoodItem  # Import the FoodItem model
from vendor.models import Vendor  # Import the Vendor model

# Global variable to store the request object
request_object = ''

# Define the Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # ForeignKey to the User model, allows null values
    vendors = models.ManyToManyField(Vendor, blank=True)  # ManyToManyField to the Vendor model, can be blank
    order_number = models.CharField(max_length=50, unique=True)  # Unique order number
    first_name = models.CharField(max_length=50)  # First name of the customer
    last_name = models.CharField(max_length=50)  # Last name of the customer
    phone = models.CharField(max_length=20)  # Phone number of the customer
    email = models.EmailField()  # Email address of the customer
    address = models.CharField(max_length=255)  # Address of the customer
    city = models.CharField(max_length=50)  # City of the customer
    state = models.CharField(max_length=50)  # State of the customer
    pin_code = models.CharField(max_length=10)  # Pin code of the customer's address
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order
    created_at = models.DateField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateField(auto_now=True)  # Automatically set the field to now every time the object is saved
    total_data = models.JSONField(blank=True, null=True)  # JSON field to store total data, can be blank or null
    tax_data = models.JSONField(blank=True, null=True)  # JSON field to store tax data, can be blank or null

    # String representation of the Order model
    def __str__(self):
        return self.order_number

    # Method to get total and tax details by vendor
    def get_total_by_vendor(self):
        vendor = Vendor.objects.get(user=request_object.user)  # Get the vendor associated with the current user
        subtotal = 0
        tax = 0
        tax_dict = {}
        if self.total_data:
            total_data = json.loads(self.total_data)  # Load total data from JSON
            data = total_data.get(str(vendor.id))  # Get the data for the specific vendor

            # Calculate subtotal and tax
            for key, val in data.items():
                subtotal += float(key)
                val = val.replace("'", '"')
                val = json.loads(val)
                tax_dict.update(val)

                # Calculate tax from tax data
                for i in val:
                    for j in val[i]:
                        tax += float(val[i][j])
        grand_total = float(subtotal) + float(tax)  # Calculate grand total
        context = {
            'subtotal': subtotal,
            'tax_dict': tax_dict,
            'grand_total': grand_total,
        }

        return context

    # Method to get a list of vendors associated with the order
    def order_placed_to(self):
        return ", ".join([str(i) for i in self.vendors.all()])  # Join the vendor names with a comma

# Define the OrderedFood model
class OrderedFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # ForeignKey to the Order model, cascade on delete
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model, cascade on delete
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # ForeignKey to the FoodItem model, cascade on delete
    quantity = models.IntegerField()  # Quantity of the food item
    price = models.FloatField()  # Price of the food item
    amount = models.FloatField()  # Total amount for the food item (quantity * price)
    created_at = models.DateField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateField(auto_now=True)  # Automatically set the field to now every time the object is saved

    # String representation of the OrderedFood model
    def __str__(self):
        return self.fooditem.food_title  # Return the title of the food item
