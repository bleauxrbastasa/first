from django.db import models

# Create your models here.

class inventoryItem(models.Model):
	name = models.CharField(max_length = 100, null=True)
	description = models.CharField(max_length = 200, null=True)
	quantity = models.FloatField(null=True)
	item_pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name