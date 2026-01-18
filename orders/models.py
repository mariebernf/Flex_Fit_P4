from django.db import models
import uuid
from products.models import Product
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    order_number = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        editable=False,
        unique=True
    )

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"

class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='lineitems',
        on_delete=models.CASCADE
    )
 
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        editable=False
    )

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} ({self.size}) x {self.quantity}'
