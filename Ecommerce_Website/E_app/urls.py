from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
]

