
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    food_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name
