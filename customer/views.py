from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import User
from .models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User as DjangoUser
from .models import Product
from django.shortcuts import render
from inventory.models import inventoryItem
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("Entered Email:", email)  # Debugging output
        print("Entered Password:", password)  # Debugging output

      
        user = User.objects.filter(email=email).first()

        print("Database Email:", user.email if user else None)  # Debugging output
        print("Database Password:", user.password if user else None)  # Debugging output

      
        if user.email == email and user.password == password:
           return redirect('customer:customer_dashboard')

    return render(request, 'customerLogin.html')


def customer_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            return render(request, 'customerSignUp.html', {'error': 'Passwords do not match'})

        if User.objects.filter(name=name).exists():
            messages.error(request, 'Name already in use. Please try again.')
            return redirect('customer_signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use. Please try again.')
            return redirect('customer_signup')
        else:
            new_user = User(name=name, email=email, password=password)
            new_user.save()
            
            messages.success(request, 'Registration successful. Please login.')  

            return redirect('customer:customer_login')

    return render(request, 'customerSignUp.html')

def customer_dashboard(request):
    items = inventoryItem.objects.all()  # Fetch all inventory items
    return render(request, 'customerDashboard.html', {'items': items})

def customer_about(request):
    
    return render(request, 'customerAbout.html')  # Point to the correct template

def view_products(request):
    products = Product.objects.all()  # Fetches all products from the database
    return render(request, 'view-products.html', {'products': products})

def orders(request):
    # Logic for displaying user orders
    return render(request, 'customerOrderStatus.html')  # Ensure you have this template

def payment_options(request):
    # Logic for displaying payment options
    return render(request, 'customerPaymentOption.html')  # Ensure you have this template

def delivery_settings(request):
    # Logic for displaying and updating delivery settings
    return render(request, 'customerDeliverySettings.html')  # Ensure you have this template

def support_messages(request):
    # Logic for displaying support messages
    return render(request, 'customerMessages.html')  # Ensure you have this template

def view_users(request):
    users = User.objects.all()  
    return render(request, 'view_users.html', {'users': users})




# Your other view functions...

@require_POST
def set_delivery_options(request):
    # Example implementation, adjust according to your models and needs
    if request.user.is_authenticated:
        # Logic to update the user's delivery options based on form data
        # You might access form data using request.POST.get('<field_name>')
        # e.g., address = request.POST.get('address')
        
        # After updating the options, redirect to a confirmation page or back to the form
        return redirect('delivery_settings')  # Redirect to the delivery settings page
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('customer_login')






# Import any necessary models or utilities

# from django.shortcuts import render
# from .models import Message  # Adjust the import according to your app structure

# def support_messages(request):
#     # Ensure the user is authenticated
#     if not request.user.is_authenticated:
#         return redirect('customer_login')

#     # Fetch message history for the current user
#     # Adjust the query to match your data model and relationships
#     messages = Message.objects.filter(recipient=request.user).order_by('-date_sent')

#     context = {
#         'messages': messages,
#     }
#     return render(request, 'customerMessages.html', context)




@require_POST
def send_message(request):
    # Implement the logic to handle the message submission
    # This might involve saving the message to the database
    
    # Make sure to check if the user is authenticated (if necessary)
    if not request.user.is_authenticated:
        return redirect('customer_login')  # Or wherever you want unauthenticated users to go

    # Example logic (adapt based on your model and fields)
    message_content = request.POST.get('message')
    if message_content:
        # Assuming you have a Message model and a way to identify the sender
        # Message.objects.create(content=message_content, sender=request.user)

        return redirect('customer_messages')  # Redirect to the messages page or confirmation page
    else:
        # Handle the case where the message is empty or invalid
        return HttpResponse('Invalid message content', status=400)



# customer/views.py

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CartItem



@csrf_exempt
def save_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        items_saved = []
        for item in data.get('cartItems', []):
            name = item.get('name')
            price = item.get('price')  # No need to check if it's None; the model allows null
            quantity = item.get('quantity', 1)  # Default to 1 if quantity is missing

            cart_item = CartItem.objects.create(name=name, price=price, quantity=quantity)
            items_saved.append(cart_item.name)

        return JsonResponse({'message': f"Cart saved successfully! Items saved: {items_saved}"}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)



def customer_home(request):
    # Home page view, possibly a landing page or product listing
    items = inventoryItem.objects.all()  # Retrieve all products from the database
    return render(request, 'customer_home.html', {'items': items})

def cart_view(request):
    # Your cart handling logic here
    return render(request, 'cart.html')  # Update with your actual cart template