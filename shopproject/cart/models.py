from django.db import models
from shopapp.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    data_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering = ['data_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)