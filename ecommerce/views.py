
from email import message
import datetime
from math import prod
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from django.conf import settings
from .models import Cart, Category, SubCategory
from django.contrib.auth import authenticate, login


#Authentication
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login successfully")
    else:
        return message.error(request, "Invalid username or Password")


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
        return message.error(request, "Invalid username or Password")
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
