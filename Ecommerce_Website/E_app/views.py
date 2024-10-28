from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# --------------------------------------------------------------------------------------------------------------------

# signup funtion
def signup(request):
    if request.method == 'POST':
        # Ensure this block is indented correctly
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

# --------------------------------------------------------------------------------------------------------------------

# login function
def login_view(request):
    if request.method == 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password) 
       if user is not None:
          login(request, user)
        #   return redirect('main.html')
          return render(request, 'main.html')
       else:
          return render(request, 'login.html', {'error': 'Invalid Credentials'})
    else:
       return render(request, 'login.html')

# --------------------------------------------------------------------------------------------------------------------

# main function
def main(request):
    return render(request, 'main.html')

# --------------------------------------------------------------------------------------------------------------------

# Home page
def home(request):
    return render(request, 'home.html')

# --------------------------------------------------------------------------------------------------------------------

# Products page
def product(request):
    return render(request, 'product.html')

# --------------------------------------------------------------------------------------------------------------------

# About us page
def about_us(request):
    return render(request, 'about_us.html')

# --------------------------------------------------------------------------------------------------------------------

# contact page
def contact(request):
    return render(request, 'contact.html')

# --------------------------------------------------------------------------------------------------------------------

from django.http import HttpResponse
from .models import User_Cart, Product

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        
        # Assuming you have a Cart model to handle cart items
        cart = User_Cart.objects.get(user=request.user)
        cart.products.add(product)  # Add product to the cart
        
        return redirect('product_list')  # Redirect to the product list or wherever appropriate
    return HttpResponse(status=405)  # Method not allowed if not POST
