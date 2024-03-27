from django.urls import path
from accounts import views as user_views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth.views import LogoutView
# from .views import register, user_login, user_logout

urlpatterns = [
    path('signup/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('logout/', user_views.logout, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', user_views.contact, name='contact'),
    path('home/', user_views.home, name='home'),
    # path('dashboard/', user_views.dashboard, name='dashboard'),
    path('about/', user_views.about, name='about'),
    path('profile/', user_views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

