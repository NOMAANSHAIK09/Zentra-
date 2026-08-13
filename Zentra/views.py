from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')

def myorder(request):
    return render(request, 'myorder.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def message(request):
    return render(request, 'message.html')

def profile(request):
    return render(request, 'profile.html')

def storeprofile(request):
    return render(request, 'storeprofile.html')

def checkout(request):
    return render(request, 'checkout.html')

def addproduct(request):
    return render(request, 'addproduct.html')



