from django.db import models
import uuid
class inventoryItem(models.Model):
    VENDOR_CHOICES = [
        ('Boy Bondat', 'Boy Bondat'),
        ('Mang Boks', 'Mang Boks'),
        ('Potato King', 'Potato King'),
        ('Siomai King', 'Siomai King'),
        ('Siopao Da King', 'Siopao Da King'),
    ]

    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vendor = models.CharField(max_length=100, choices=VENDOR_CHOICES)
    item_pic = models.ImageField(null=True, blank=True)
    expiry_date = models.DateField(null=True) 
    
    def __str__(self):
        return self.name

class ScheduledDelivery(models.Model):
    tracking_id = models.CharField(max_length=100)
    delivery_status_choices = [
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
    ]
    delivery_status = models.CharField(max_length=20, choices=delivery_status_choices, default='In Transit')
    payment_type_choices = [
        ('COD', 'Cash on Delivery')
    ]
    payment_type = models.CharField(max_length=10, choices=payment_type_choices, default='COD')
    
    def __str__(self):
        return self.tracking_id

class Order(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(inventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Order for {self.name} - {self.product.name}"