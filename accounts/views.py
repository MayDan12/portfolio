# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
# from hive_manager.models import Hive, Membership
from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class CustomLogoutView(View):
    @method_decorator(csrf_exempt)  # Disable CSRF token for demonstration purposes
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to a login page or your custom logout page


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created you can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# user must be logged in to view profile
@login_required
def user_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')  # Redirect to profile update form
    else:
        user_update_form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/user_update.html', {'user_update_form': user_update_form})



def profile_update(request):
    if request.method == 'POST':
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')  # Redirect to profile update form
    else:
        profile_update_form = ProfileUpdateForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile_update.html', {'profile_update_form': profile_update_form})






# def profile(request):
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

#         # if user_form.is_valid() and profile_form.is_valid:
#         #save only profile picture
#             # user_form.save()

#         if user_form.is_valid() and profile_form.is_valid:

#             user_form.save()
#             profile_form.save()

#             messages.success(request, f'Account Updated!')
#             return redirect('profile')

#     else:
#         # forms for user info and profile picture update
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.userprofile)

#     dummy = {
#         'user_form': user_form,
#         'profile_form': profile_form
#     }

#     return render(request, 'accounts/profile.html', dummy)



def contact(request):
    return render(request, 'accounts/contact.html')

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')


























# @csrf_protect
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})

# def logout(request):
#     logout(request)
#     return redirect('home')

# def logout_view(request):
#     logout(request)
#     return redirect('login')
