from django.urls import path, include

from . import views

# Cart Urls
urlpatterns = [
    path('', views.Homepage.as_view(), name="homepage"),
    path('cart/', views.ListCart.as_view(), name='list-carts'),
    path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    path('cart/order/', views.OrderCart.as_view(), name='order-cart'),
    path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
    path('cart/create/', views.CreateNewCart.as_view(), name='create-new-cart')
]



