from django.shortcuts import render, redirect

from Zentra.models import userinfo

# Create your views here.


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = userinfo.objects.get(email=email, password=password)
            # User found, redirect to home page
            return redirect('home')
        except userinfo.DoesNotExist:
            # User not found, display an error message
            error_message = "Invalid email or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users=userinfo(name=name, email=email, password=password)
        users.save()
        
        return redirect('home')  
    
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



