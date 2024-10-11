
# Multi-Vendor Food Ordering System

This Django-based web application enables multiple vendors to list food items for customers to order. The system provides a secure and user-friendly platform where customers can browse food items, manage their cart, and complete orders, while vendors can manage their food listings and view incoming orders. The application also features role-based access control, ensuring different permissions for customers, vendors, and administrators.

## Customer Features

- **Secure Login & Signup** : Customers can securely sign up and log in to the platform.
- **Profile Management** : Customers can edit their profile, including phone number, email, address, and profile picture, through a dedicated dashboard.
- **Food Ordering** : Browse food items listed by vendors and add them to the cart.
- **Marketplace** : Customers can order food through marketplace where all athe resturents are listed 
- **Cart Management** : Easily manage the cart by adding or removing items.
- **Checkout** : Secure checkout process for placing orders.
- **Order Confirmation Email** : Customers receive an email listing the food items ordered once an order is placed.
- **Forgot Password** : Users can reset their password by clicking "Forgot Password." An email with a reset link is sent to their registered email for easy password change

## Vendor Features

- **Secure Login & Signup** : Vendors can sign up and manage their accounts.
- **Order Notifications** : Vendors receive an email with the order details once an order is placed.
- **Food Item Management** : Vendors can list, update, and remove food items they wish to sell.
- **Vendor Dashboard** : Vendors can manage their listings and view incoming orders.
-  **Forgot Password** : Users can reset their password by clicking "Forgot Password." An email with a reset link is sent to their registered email for easy password change

## Admin Features

- **Role-Based Access Control** : Admins can manage users, including vendors and customers, assigning specific permissions as needed.

## Additional Functionalities

- **Email Notifications** : Integrated email system to notify customers and vendors of order details.
- **SQL Database** : All customer, vendor, and order data is stored in an SQL database.

## SMTP Configuration

Create a .env file in the project root to store environment variables like the SECRET_KEY and email configuration settings. For example:

- **SECRET_KEY=your-secret-key**
- **EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend**
- **EMAIL_HOST=smtp.your-email-host.com**
- **EMAIL_PORT=587**
- **EMAIL_USE_TLS=True**
- **EMAIL_HOST_USER=your-email@example.com**
- **EMAIL_HOST_PASSWORD=your-email-password**






