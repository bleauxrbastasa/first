from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ItemForm
from datetime import datetime, timedelta


# Create your views here.

def home(request):
	return render(request, 'inventory/dashboard.html')

def inventory(request):
	item = inventoryItem.objects.all()
	return render(request, 'inventory/inventory.html', {'item': item})

def customer(request):
	return render(request, 'inventory/customer.html')

def createItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    context = {'form': form}
    return render(request, 'inventory/item_form.html', context)


def updateItem(request, pk):
    item = inventoryItem.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    context = {'form': form}
    return render(request, 'inventory/item_form.html', context)

def deleteItem(request, pk):
	item = inventoryItem.objects.get(id=pk)

	if request.method == "POST":
		item.delete()
		return redirect('inventory')
	context = {'item': item}
	return render(request, 'inventory/delete.html', context)

def expiry_view(request):
    current_date = datetime.now().date()
    one_month_from_now = current_date + timedelta(days=30)

    expiring_items = inventoryItem.objects.filter(expiry_date__gte=current_date, expiry_date__lte=one_month_from_now)

    return render(request, 'inventory/expiry.html', {'expiring_items': expiring_items})