from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Define a custom middleware class to handle PermissionDenied exceptions
class CustomPermissionDeniedMiddleware:
    def __init__(self, get_response):
        # Middleware initialization method
        # get_response is the next middleware or view to be called
        self.get_response = get_response

    def __call__(self, request):
        # This method is called for each request
        response = self.get_response(request)  # Process the request and get the response
        return response  # Return the response

    def process_exception(self, request, exception):
        # This method is called when an exception occurs during request processing
        if isinstance(exception, PermissionDenied):
            # If the exception is of type PermissionDenied, render a custom 403 error page
            return render(request, '403.html', {'message': str(exception)}, status=403)
        return None  # For other exceptions, do nothing and return None
