from django.urls import path
from accounts import views as user_views
# from .views import register, user_login, user_logout

urlpatterns = [
    path('signup/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('contact/', user_views.contact, name='contact'),
    path('home/', user_views.home, name='home'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('about/', user_views.about, name='about'),
]
