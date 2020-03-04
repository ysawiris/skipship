from django.urls import path, include

from . import views

app_name = 'cartitem'


urlpatterns=[
    path('all/<int:pk>', views.DetailCartItem.as_view(), name='detail-cartitem'),
    path('all/', views.ListCartItem.as_view(), name='list-cartitem'),
    path('create/', views.CreateNewCartItem.as_view(), name='create-cartitem'),
    path('all/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('all/<int:pk>/delete/', views.deleteCartItem, name='delete-cartitem'),
]