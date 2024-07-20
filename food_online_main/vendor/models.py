from django.db import models
from accounts.models import User, UserProfile
from accounts.utils import send_notification
from datetime import time

class Vendor(models.Model):
    # Link the Vendor model to a User model instance
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    
    # Link the Vendor model to a UserProfile model instance
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    
    # Field to store the vendor's name
    vendor_name = models.CharField(max_length=50)
    
    # Field to store a unique slug for the vendor
    vendor_slug = models.SlugField(max_length=100, unique=True)
    
    # Field to store the vendor's license image
    vendor_license = models.ImageField(upload_to='vendor/license')
    
    # Boolean field to indicate if the vendor is approved
    is_approved = models.BooleanField(default=False)
    
    # Automatically set the field to now when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically set the field to now every time the object is saved
    modified_at = models.DateTimeField(auto_now=True)

    # Return the vendor's name as the string representation of the model
    def __str__(self):
        return self.vendor_name

    # Override the save method to add custom behavior when saving
    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Vendor.objects.get(pk=self.pk)
            # Check if the approval status has changed
            if orig.is_approved != self.is_approved:
                mail_template = 'accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                    'to_email': self.user.email,
                }
                if self.is_approved:
                    # Send approval notification email
                    mail_subject = "Congratulations! Your restaurant has been approved."
                    send_notification(mail_subject, mail_template, context)
                else:
                    # Send disapproval notification email
                    mail_subject = "We're sorry! You are not eligible for publishing your food menu on our marketplace."
                    send_notification(mail_subject, mail_template, context)
        return super(Vendor, self).save(*args, **kwargs)
