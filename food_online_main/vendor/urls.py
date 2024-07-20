from django.urls import path, include
from . import views
from accounts import views as Accountviews

urlpatterns = [
    # Redirect to vendor dashboard
    path('', Accountviews.vendorDashboard, name='vendor'),
    
    # Vendor profile page
    path('profile/', views.vprofile, name='vprofile'),
    
    # Menu builder page
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    
    # Food items by category
    path('menu-builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),
    
    # Category CRUD (Create, Read, Update, Delete) operations
    # Add new category
    path('menu-builder/category/add/', views.add_category, name='add_category'),
    
    # Edit an existing category
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    
    # Delete a category
    path('menu-builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    
    # Add new food item
    path('menu-builder/food/add/', views.add_food, name='add_food'),
    
    # Edit an existing food item
    path('menu-builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    
    # Delete a food item
    path('menu-builder/food/delete/<int:pk>/', views.delete_food, name='delete_food'),
    
    # Order confirmation page
    path('order_confirmation/<int:order_number>/', views.order_confirmation, name='order_confirmation'),
    
    # View vendor orders
    path('my_order/', views.my_order, name='vendor_my_order'),
]
