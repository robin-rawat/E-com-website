from django.urls import path, include
from .views import HomeView, ItemDetailView, add_to_cart, remove_from_cart, OrderSummaryView, remove_item_from_cart, CheckoutView

app_name = 'core'

urlpatterns = [
    path('/', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('order-summary/',OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/',remove_item_from_cart, name='remove-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    
]