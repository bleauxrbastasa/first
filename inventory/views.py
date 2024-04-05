from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = FoodForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'inventory/product_list.html', {'foods': foods})
