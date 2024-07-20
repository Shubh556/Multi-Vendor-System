# Importing the path function from the django.urls module
from django.urls import path
# Importing the views from the current application
from . import views

# Defining the URL patterns for the application
urlpatterns = [
    # URL pattern for the marketplace view
    path('', views.marketplace, name='marketplace'),
    
    # URL pattern for the vendor detail view, expects a vendor_slug parameter
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),

    # URL pattern for adding a food item to the cart, expects a food_id parameter
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    
    # URL pattern for decreasing the quantity of a food item in the cart, expects a food_id parameter
    path('decrease_cart/<int:food_id>/', views.decrease_cart, name='decrease_cart'),
    
    # URL pattern for deleting a cart item, expects a cart_id parameter
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),
]
