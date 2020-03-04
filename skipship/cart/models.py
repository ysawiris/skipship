from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Cart(models.Model):
    cart_name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True, help_text="The date and time this cart was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date and time this cart was updated. Automatically generated when the model updates.")

