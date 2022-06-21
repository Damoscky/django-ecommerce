from queue import Empty
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
import datetime
from math import prod
from django.forms import EmailField
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.conf import settings
from .models import Cart, Category, SubCategory
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


#Authentication
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user == None:
        messages.error(request, "Invalid username or Password")
        return render(request, 'auth/login-page.html')
    else:
        messages.success(request, "You're logged in successfully")
        return render(request, '')


def signUp(request):
    usernameExist = User.objects.filter(username = request.POST['username']).exists()
    emailExist = User.objects.filter(email = request.POST['email']).exists()
    if usernameExist:
        messages.warning(request, 'Username already exist')
        return render(request, "auth/create-account.html")

    if not emailExist:
        user = User(
            username=request.POST['username'], 
            email=request.POST['email'], 
            password=request.POST['password'],
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname']
        )
        user.save()    
        if user == None:
            messages.warning(request, 'Record not created')
            return render(request, "auth/create-account.html")
        else:
            messages.success(request, 'Record created successfully')
            return render(request, "auth/create-account.html")
    else:
        messages.warning(request, 'Email already exist')
        return render(request, "auth/create-account.html")

    # if user == None:
    #     messages.error(request, "User not created")
    #     return render(request, "auth/create-account.html")
    # else:
    #     messages.success(request, "Account created successfully")
    #     return render(request, "auth/create-account.html")

def loginPage(request):
    return render(request, 'auth/login-page.html')


def createAccount(request):
    return render(request, 'auth/create-account.html')


def index(request):
    today = datetime.date.today()
    categories = Category.objects.order_by('-name')
    featuredProducts = Product.objects.filter(featured=True).order_by('-created_at')[:10]
    bestSellerProducts = Product.objects.order_by('-views')[:10]
    newProducts = Product.objects.all().order_by('-created_at')[:10]
    return render(request, 'home/index.html', {'newProducts': newProducts, 'featuredProducts': featuredProducts, 'bestSellerProducts': bestSellerProducts, 'categories': categories})
    # return HttpResponse("hello")

def allProducts(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'home/all-products.html', {'products': products})

def productQuickView(request, id):
    try:
        product = Product.objects.get(pk=id)
    except:
        messages.error(request, "Invalid username or Password")
        return render(request, 'home/index.html')
    return render(request, 'home/product-quick-view.html', {'product': product})


def contact(request):
    return render(request, 'home/contact.html')

def productDetails(request, id):
    try:
        product = Product.objects.get(pk=id)
    except:
        raise Http404("Invalid product Id")
    return render(request, 'home/product-details.html', {'product': product})

def addToCart(Request, id):
    try:
        product = Product.objects.get(pk=id)
    except:
        return Http404("Invalid Product Id")
    # return HttpResponse(product)
    cart = Cart(
        product_id = product.id,
        user_id = settings.AUTH_USER_MODEL,
        quantity = 1,
        price = product.new_price,
        total_price = product.new_price * 1
    )
    cart.save()
    return HttpResponseRedirect('home/all-product.html')
