from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

# Function to determine where to redirect the user based on their role
def detectUser(user):
    # Check the role of the user and return the corresponding dashboard URL
    if user.role == 1:
        redirectUrl = 'vendorDashboard'  # Vendor dashboard URL
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'  # Customer dashboard URL
        return redirectUrl
    elif user.role is None and user.is_superadmin:
        redirectUrl = '/admin'  # Admin panel URL
        return redirectUrl

# Function to send a verification email to the user
def send_verification_email(request, user, mail_subject, email_template):
    # Get the sender email address from settings
    from_email = settings.DEFAULT_FROM_EMAIL
    
    # Get the current site domain
    current_site = get_current_site(request)
    
    # Render the email template with user and token data
    message = render_to_string(email_template, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # Encode user ID
        'token': default_token_generator.make_token(user),  # Generate a token for verification
    })
    
    # Define the recipient email address
    to_email = user.email
    
    # Create and send the email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"  # Set the email content type to HTML
    mail.send()  # Send the email

# Function to send a general notification email
def send_notification(mail_subject, mail_template, context):
    # Get the sender email address from settings
    from_email = settings.DEFAULT_FROM_EMAIL
    
    # Render the email template with the provided context data
    message = render_to_string(mail_template, context)
    
    # Ensure the recipient email(s) is in list format
    if isinstance(context['to_email'], str):
        to_email = [context['to_email']]  # Convert single email string to list
    else:
        to_email = context['to_email']  # Use the list of emails directly
    
    # Create and send the email
    mail = EmailMessage(mail_subject, message, from_email, to=to_email)
    mail.content_subtype = "html"  # Set the email content type to HTML
    mail.send()  # Send the email
