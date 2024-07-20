from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# This function is triggered after a User instance is saved
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)  # Print whether the user was newly created or updated

    if created:
        # If the user was just created, create a corresponding UserProfile
        UserProfile.objects.create(user=instance)
    else:
        # If the user was updated, try to get the existing UserProfile
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()  # Save the profile (though this is redundant if no changes are made)
        except UserProfile.DoesNotExist:
            # If the UserProfile does not exist, create it
            UserProfile.objects.create(user=instance)
