from django.urls import path, include
from . import views  # Import the views module from the current directory

urlpatterns = [
    # Route for the home page or main account page
    path('', views.myAccount),

    # Route for user registration
    path('registerUser/', views.registerUser, name='registerUser'),

    # Route for vendor registration
    path('registerVendor/', views.registerVendor, name='registerVendor'),

    # Route for user login
    path('login/', views.login, name='login'),

    # Route for user logout
    path('logout/', views.logout, name='logout'),

    # Route for viewing the user's account details
    path('myAccount/', views.myAccount, name='myAccount'),

    # Route for the customer dashboard
    path('custDashboard/', views.custDashboard, name='custDashboard'),

    # Route for the vendor dashboard
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),

    # Route for user account activation (usually sent via email with a unique link)
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # Route for the forgot password page
    path('forgot_password', views.forgot_password, name='forgot_password'),

    # Route for validating password reset (usually sent via email with a unique link)
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),

    # Route for resetting the password
    path('reset_password', views.reset_password, name='reset_password'),

    # Include URLs from the 'vendor' app
    path('vendor/', include('vendor.urls')),

    # Include URLs from the 'customers' app
    path('customer/', include('customers.urls')),
]
