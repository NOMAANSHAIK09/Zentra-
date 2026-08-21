from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import Profile


def index(request):
    return render(request, 'index.html')


def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(
                request,
                'login.html',
                {'error_message': 'Invalid email or password'}
            )

        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        return render(
            request,
            'login.html',
            {'error_message': 'Invalid email or password'}
        )

    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        address = request.POST.get('address', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '')
        # confirm_password = request.POST.get('confirmPassword', '')

        # Password confirmation
        # if password != confirm_password:
        #     return render(
        #         request,
        #         'signup.html',
        #         {
        #             'error_message': 'Passwords do not match.',
        #             'name': name,
        #             'email': email,
        #             'address': address,
        #             'phone': phone,
        #         }
        #     )

        # Check existing email
        if User.objects.filter(email=email).exists():
            return render(
                request,
                'signup.html',
                {
                    'error_message': 'An account with this email already exists.',
                    'name': name,
                    'email': email,
                    'address': address,
                    'phone': phone,
                }
            )

        # Use email as username
        username = email

        # Django automatically hashes the password
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create Zentra profile
        Profile.objects.create(
            user=user,
            full_name=name,
            phone=phone,
            address=address
        )

        # Automatically log in
        auth_login(request, user)

        return redirect('home')

    return render(request, 'signup.html')


def logout_view(request):

    auth_logout(request)

    return redirect('login')


@login_required
def home(request):
    
    return render(request, 'home.html',
                  {
                              'user': request.user,
                              'profile': request.user.profile
                          })


@login_required
def myorder(request):
    return render(request, 'myorder.html')


@login_required
def cart(request):
    return render(request, 'cart.html')


@login_required
def wishlist(request):
    return render(request, 'wishlist.html')


@login_required
def message(request):
    return render(request, 'message.html')


@login_required
def profile(request):

    return render(
        request,
        'profile.html',
        {
            'user': request.user,
            'profile': request.user.profile
        }
    )


@login_required
def storeprofile(request):
    return render(request, 'storeprofile.html')


@login_required
def checkout(request):
    return render(request, 'checkout.html')


@login_required
def addproduct(request):
    return render(request, 'addproduct.html')