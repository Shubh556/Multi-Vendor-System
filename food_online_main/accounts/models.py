from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields.related import ForeignKey, OneToOneField

# Manager for handling user creation
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        # Ensure the user has an email and username
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')

        # Create and save a new user
        user = self.model(
            email=self.normalize_email(email),  # Normalize email (lowercase)
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  # Set the user's password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        # Create a new superuser with admin, staff, and superadmin rights
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    # Choices for user roles
    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )

    # User fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # Required fields for tracking dates and user status
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Specify the email field as the username field for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()  # Use the custom UserManager

    def __str__(self):
        return self.email  # Return email as the string representation of the user

    def has_perm(self, perm, obj=None):
        # Check if the user has a specific permission (admin users have all permissions)
        return self.is_admin

    def has_module_perms(self, app_label):
        # Check if the user has permissions for a given app (admins have all permissions)
        return True

    @property
    def full_name(self):
        # Return the user's full name as "first_name last_name"
        return f"{self.first_name} {self.last_name}"

# User profile model, linked one-to-one with the User model
class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)  # Link to User model
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email  # Return the user's email as the string representation of the profile

    def get_role(self):
        # Return the user's role as a string based on the role value
        if self.user.role == User.VENDOR:
            return 'Vendor'
        elif self.user.role == User.CUSTOMER:
            return 'Customer'
        return 'Unknown'

    @property
    def full_name(self):
        # Return the full name of the user associated with this profile
        return self.user.full_name
