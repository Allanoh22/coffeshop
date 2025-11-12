from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)  
    description = models.TextField()
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    status = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(MenuItem)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"