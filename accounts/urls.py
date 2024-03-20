from django.urls import path
from . import views
from .views import register, user_login, user_logout

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
