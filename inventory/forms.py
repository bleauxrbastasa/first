from django import forms
from .models import inventoryItem

class ItemForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = inventoryItem
        fields = '__all__'