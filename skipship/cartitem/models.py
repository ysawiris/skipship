from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from cart.models import Cart

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
# model_variable = models.ForeignKey('the_appname.the_model_class_name)
   

    # def price_ttc(self):
    #     TAX_AMOUNT = 19.25
    #     return self.price_ht * (1 + TAX_AMOUNT/100.0)

    # def __str__(self):
    #     return  self.user + " - " + self.product