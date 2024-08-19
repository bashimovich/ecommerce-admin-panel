from django.db import models
from ecommerce.models import Product
from django.contrib.auth.models import User

# Create your models here.
from random import randint


def random_str():
    _str = ''
    for i in range(10):
        a, b, c = randint(65, 90), randint(
            48, 57), randint(97, 122)
        if b > 53:
            _str += chr(a) + chr(b) + chr(c)
        else:
            _str += chr(b) + chr(a) + chr(c)
    if Order.objects.filter(number=_str).first() is None:
        return _str
    else:
        random_str()


class Cart(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cart')
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user_id.username


class Address(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='address')
    add = models.TextField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username


class Order(models.Model):
    STATUS_CHOICES = (
        ('1', 'PENDING'),
        ('2', 'ACCEPTED'),
        ('3', 'SENT'),
        ('4', 'DELIVERED'),
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order')
    number = models.CharField(max_length=100)
    address_id = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='order')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='1', db_index=True)
    products = models.ManyToManyField(Product, through='OrderProducts')

    def save(self, *args, **kwargs):
        if self.number == '':
            self.number = random_str()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.number


class OrderProducts(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id.number
