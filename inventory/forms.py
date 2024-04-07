from django import forms
from .models import inventoryItem
from .models import ScheduledDelivery

class ScheduledDeliveryForm(forms.ModelForm):
    class Meta:
        model = ScheduledDelivery
        fields = ['tracking_id', 'delivery_status', 'payment_type']

class ItemForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = inventoryItem
        fields = ['name', 'description', 'quantity', 'price', 'vendor', 'item_pic', 'expiry_date']

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    product = forms.ModelChoiceField(queryset=inventoryItem.objects.all())
    quantity = forms.IntegerField(min_value=1)
    address = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product'].label = "Product"
        self.fields['quantity'].label = "Quantity"