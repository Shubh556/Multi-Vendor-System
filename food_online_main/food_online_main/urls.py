from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from marketplace import views as marketplaceviews

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Home page URL
    path('', views.home, name='home'),

    # Account-related URLs
    path('', include('accounts.urls')),  # Corrected include statement

    # Marketplace-related URLs
    path('marketplace/', include('marketplace.urls')),

    # Cart page URL
    path('cart/', marketplaceviews.cart, name='cart'),

    # Search functionality URL
    path('search/', marketplaceviews.search, name='search'),

    # Checkout page URL
    path('checkout/', marketplaceviews.checkout, name='checkout'),

    # Orders-related URLs
    path('orders/', include('orders.urls')),

    # Serve media files during development
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
