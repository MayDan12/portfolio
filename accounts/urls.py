from django.urls import path
from accounts import views as user_views
# from .views import register, user_login, user_logout

urlpatterns = [
    path('signup/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('contact/', views.contact, name='contact'),
    path('home/', user_views.home, name='home'),
    # path('about/', views.about, name='about'),
]
