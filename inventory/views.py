from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ItemForm, OrderForm
from datetime import datetime, timedelta
from .forms import ScheduledDeliveryForm
from django.contrib import messages 

# Create your views here.

def home(request):
    item = inventoryItem.objects.all()
    return render(request, 'inventory/dashboard.html', {'item': item})

def inventory(request):
    items_by_vendor = {}
    vendors = set(inventoryItem.objects.values_list('vendor', flat=True))
    for vendor in vendors:
        items_by_vendor[vendor] = inventoryItem.objects.filter(vendor=vendor)
    return render(request, 'inventory/inventory.html', {'items_by_vendor': items_by_vendor})

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

def delivery_list(request):
    deliveries = ScheduledDelivery.objects.all()
    return render(request, 'inventory/delivery_list.html', {'deliveries': deliveries})

def add_scheduled_delivery(request):
    if request.method == 'POST':
        form = ScheduledDeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = ScheduledDeliveryForm()
    return render(request, 'inventory/add_scheduled_delivery.html', {'form': form})

def update_delivery_status(request):
    if request.method == 'POST':
        delivery_id = request.POST.get('delivery_id')
        new_status = request.POST.get('delivery_status')
        delivery = ScheduledDelivery.objects.get(id=delivery_id)
        delivery.delivery_status = new_status
        delivery.save()
    return redirect('delivery_list')

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            address = form.cleaned_data['address']
            
            # Fetch the selected product from the database
            selected_product = inventoryItem.objects.get(id=product.id)

            # Calculate the total price
            total_price = selected_product.price * quantity

            # Create the order
            order = Order.objects.create(
                name=form.cleaned_data['name'],
                product=selected_product,
                quantity=quantity,
                address=address
            )

            messages.success(request, f'Order for {quantity} {selected_product.name}(s) successfully placed! Total Price: ${total_price}')

            return redirect('dashboard')
    else:
        form = OrderForm()
    return render(request, 'inventory/add_order.html', {'form': form})

def all_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'inventory/all_orders.html', context)

def delete_order(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.delete()
    return redirect('all_orders')


from customer.models import CartItem
def new_order(request):
    orders = CartItem.objects.all()
    return render(request, 'inventory/new_orders.html', {'orders': orders})
	