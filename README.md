
# Project Title

A brief description of what this project does and who it's for


# Multi-Vendor Food Ordering System

This Django-based web application enables multiple vendors to list food items for customers to order. The system provides a secure and user-friendly platform where customers can browse food items, manage their cart, and complete orders, while vendors can manage their food listings and view incoming orders. The application also features role-based access control, ensuring different permissions for customers, vendors, and administrators.

## Customer Features

- **Secure Login & Signup** : Customers can securely sign up and log in to the platform.
- **Profile Management** : Customers can edit their profile, including phone number, email, address, and profile picture, through a dedicated dashboard.
- **Food Ordering** : Browse food items listed by vendors and add them to the cart.
- **Marketplace** : Customers can order food through marketplace where all the resturents are listed 
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

### Home Page

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/Home%20page.png?raw=true)

### Cutomer Signup Page 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/Customer%20reigister%20page.png?raw=true)

### Resturent Signup Page 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/resturent%20register%20page%20.png?raw=true)

### Login Page 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/sign%20in.png?raw=true)

### Customer Dashboard

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/new%20order%20for%20resturent%20.png?raw=true)


### Cutomer Order Page

![Home Pages 2](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/customers%20orders.png?raw=true)

### Edit Profile Page of Customer

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/update%20customer%20profile.png?raw=true)

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/update%20customer%20profile.png?raw=true)

### Vendor Dashboard

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/vendor%20dashboard.png?raw=true)

### Manage My Resturent Page 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/update%20resturant%20profile.png?raw=true)

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/update%20resturant%20profile-2.png?raw=true)

### Menu Builder 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/menu%20builder.png?raw=true)

### Order Page of Resturent 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/all%20orders.png?raw=true)

### Market Place 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/marketplace.png?raw=true)

### Menu of a Resturent 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/menu%20of%20a%20resturent%20.png?raw=true)

### Checkout Page

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/checkout.png?raw=true)

### Payment Page

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/payment%20page.png?raw=true)

### Billing 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/bill.png?raw=true)

### Order Recived By Resturent 

![Home Pages1](https://github.com/Shubh556/Multi-Vendor-System/blob/main/Images/new%20order%20for%20resturent%20.png?raw=true)




























