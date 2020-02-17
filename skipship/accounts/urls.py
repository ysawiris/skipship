from django.urls import path
from accounts.views import register, ProfileUpdateView

urlpatterns = [
    path('signup/', register, name='media-signup-page'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update-profile')
]