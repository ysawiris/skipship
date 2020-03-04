from django.urls import path, include

from . import views

urlpatterns=[
    path('all/', views.ListCartItem.as_view(), name='list-cartitem'),
    path('<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    path('create/', views.CreateNewCartItem.as_view(), name='create-cartitem'),
    path('<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]