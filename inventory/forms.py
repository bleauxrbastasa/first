from django.forms import ModelForm
from .models import *

class itemForm(ModelForm):
	class Meta:
		model = inventoryItem
		fields = '__all__'