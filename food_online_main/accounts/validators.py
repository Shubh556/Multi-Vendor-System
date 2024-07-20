from django.core.exceptions import ValidationError
import os

# Validator function to ensure that uploaded files are images
def allow_only_images_validator(value):
    # Get the file extension of the uploaded file
    ext = os.path.splitext(value.name)[1]  # Example: '.jpg'
    
    # Print the file extension for debugging purposes (you can remove this line in production)
    print(ext)
    
    # Define a list of valid image file extensions
    valid_extensions = ['.png', '.jpg', '.jpeg']
    
    # Check if the file extension is in the list of valid extensions
    if not ext.lower() in valid_extensions:
        # Raise a ValidationError if the file extension is not valid
        raise ValidationError(
            'Unsupported file extension. Allowed extensions: ' + str(valid_extensions)
        )
