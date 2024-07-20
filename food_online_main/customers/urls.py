from django.urls import path
# Importing views from the accounts app and the current app
from accounts import views as accountviews
from . import views

# Defining URL patterns for this app
urlpatterns = [
    # The root URL '' is mapped to the custDashboard view from accounts.views
    path('', accountviews.custDashboard, name='customer'),
    
    # URL 'profile/' is mapped to the cprofile view from the current app's views
    path('profile/', views.cprofile, name='cprofile'),
    
    # URL 'my_orders/' is mapped to the my_orders view from the current app's views
    path('my_orders/', views.my_orders, name='customer_my_orders'),
    
    # URL 'order_detail/<int:order_number>/' is mapped to the order_detail view from the current app's views
    # <int:order_number> captures an integer value from the URL and passes it to the view as a parameter
    path('order_detail/<int:order_number>/', views.order_detail, name='order_detail'),
]
