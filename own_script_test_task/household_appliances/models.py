from django.db import models
from django.db.models import Sum

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def life_time_value(self):
        return sum(order.amount() for order in self.orders.all())

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def amount(self):
        return sum(item.amount() for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def amount(self):
        return self.product.price * self.quantity