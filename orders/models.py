from django.db import models


class Order(models.Model):
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

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"


from products.models import Product

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

    def __str__(self):
        return f'{self.product.name} ({self.size}) x {self.quantity}'
