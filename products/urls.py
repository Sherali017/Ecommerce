from django.urls import path

from products.views import ProductListView, ProductDetailView, WishListListView, add_wishlist, add_to_cart

app_name='products'

urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('wishlist', WishListListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_wishlist, name='add-wishlist'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart')
]
