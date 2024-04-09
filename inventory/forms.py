from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'quantity', 'food_type', 'image']
