from django.urls import path  # Import the path function from Django's URL module
from . import views  # Import the views from the current directory

# Define the URL patterns for the orders app
urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),  # URL pattern for placing an order
    path('order_confirmation/<int:order_number>/', views.order_confirmation, name='order_confirmation'),  # URL pattern for order confirmation with the order number as a parameter
]
