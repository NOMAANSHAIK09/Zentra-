from django.contrib import admin
from django.urls import path

from Zentra.views import (
    index,
    home,
    login_view,
    logout_view,
    signup,
    myorder,
    cart,
    wishlist,
    message,
    profile,
    storeprofile,
    checkout,
    addproduct,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),

    path('home/', home, name='home'),
    path('myorder/', myorder, name='myorder'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('message/', message, name='message'),
    path('profile/', profile, name='profile'),
    path('storeprofile/', storeprofile, name='storeprofile'),
    path('checkout/', checkout, name='checkout'),
    path('addproduct/', addproduct, name='addproduct'),
]