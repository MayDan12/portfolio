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

    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'), name='password_reset'),

    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('logout/', user_views.logout, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', user_views.contact, name='contact'),
    path('', user_views.home, name='home'),
    # path('dashboard/', user_views.dashboard, name='dashboard'),
    path('about/', user_views.about, name='about'),
    path('user_update/', user_views.user_update, name='user_update'),
    path('profile/', user_views.profile, name='profile'),
    path('profile_update/', user_views.profile_update, name='profile_update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

