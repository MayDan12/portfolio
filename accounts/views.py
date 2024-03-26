from django.contrib.auth.forms import UserCreationForm
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


class CustomLogoutView(View):
    @method_decorator(csrf_exempt)  # Disable CSRF token for demonstration purposes
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to a login page or your custom logout page


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created you can now login!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

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

# user must be logged in to view profile
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

# @login_required
# def dashboard(request):
#     # Fetch data from models
#     # tasks = Task.objects.all()
#     hives = Hive.objects.all()
#     memberships = Membership.objects.all()

#     context = {
#         # 'tasks': tasks,
#         'hives': hives,
#         'memberships': memberships,
#     }
#     return render(request, 'accounts/dashboard.html', context)

