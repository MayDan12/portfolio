# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Hive, Membership, Task, Event
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreateHiveForm, CreateTaskForm


@login_required
def dashboard(request):
    hive_id=...
    # Fetch data from models
    hive_form = CreateHiveForm()
    task_form = CreateTaskForm()
    tasks = Task.objects.all()
    hives = Hive.objects.all()
    memberships = Membership.objects.all()
    events = Event.objects.all()  # Query all events from the database

    context = {
        'hive_form': hive_form,
        # 'hive_id': hive_id,
        'task_form': task_form,
        'tasks': tasks,
        'hives': hives,
        'memberships': memberships,
        'events': events
    }
    return render(request, 'hive_manager/dashboard.html', context)



def hive_memberships(request, hive_id):
    hive = Hive.objects.get(pk=hive_id)
    memberships = Membership.objects.filter(hive=hive)
    return render(request, 'hive_manager/hive_memberships.html', {'hive': hive, 'memberships': memberships})


# view Hive manager

class HiveListView(LoginRequiredMixin, ListView):
    model = Hive
    template_name = 'hive_manager/hive_list.html'
    context_object_name = 'hives'
    order = ['-StarDate']
    paginate_by = 2

    def get_queryset(self):
        # Return an ordered QuerySet
        return Hive.objects.all().order_by('-StartDate')



class UserHiveListView(LoginRequiredMixin, ListView):
    model = Hive
    template_name = 'hive_manager/user_hive_list.html'
    context_object_name = 'hives'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Hive.objects.filter(HiveOwner=user).order_by('-StartDate')


class HiveDetailView(LoginRequiredMixin, DetailView):
    model = Hive
    template_name = 'hive_manager/hive_detail.html'
    # context_object_name = 'hives'
    # order = ['-StarDate']

class HiveCreateView(LoginRequiredMixin, CreateView):
    model = Hive
    hive_form = CreateHiveForm()
    fields = ['title', 'description','intendedUsers', 'status', 'StartDate', 'EndDate']
    template_name = 'hive_manager/create_hive.html'
    context_object_name = 'hives'

    # order = ['-StarDate']

    def form_valid(self, form):
        form.instance.HiveOwner = self.request.user
        return super().form_valid(form)

class HiveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Hive
    fields = ['title', 'description','intendedUsers', 'status', 'StartDate', 'EndDate']
    template_name = 'hive_manager/update_hive.html'
    context_object_name = 'hives'
    # order = ['-StarDate']

    def form_valid(self, form):
        form.instance.HiveOwner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        hive = self.get_object()
        if self.request.user == hive.HiveOwner:
            return True
        return False

class HiveDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hive
    template_name = 'hive_manager/delete_hive.html'
    success_url = reverse_lazy('dashboard')
    # context_object_name = 'hives'
    # order = ['-StarDate']

    # user passes Test to be able to delete hive
    def test_func(self):
        hive = self.get_object()
        if self.request.user == hive.HiveOwner:
            return True
        return False




# View Task manager

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'hive_manager/task_list.html'
    context_object_name = 'tasks'
    order = ['-StarDate']


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'hive_manager/task_detail.html'
    # context_object_name = 'tasks'
    order = ['-StarDate']

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    task_form = CreateTaskForm()
    fields = ['hive', 'title', 'description', 'assignedTo', 'StartDate', 'EndDate']
    template_name = 'hive_manager/dashboard.html'
    # context_object_name = 'hives'
    # order = ['-StarDate']

    def dispatch(self, request, *args, **kwargs):
        # Retrieve the hive ID from the URL parameters
        hive_id = self.kwargs.get('hive_id')
        # Retrieve the hive object based on the hive ID
        hive = Hive.objects.get(id=hive_id)

        # Check if the current user is a member of the hive
        if not request.user in hive.memberships.all():
            # If the user is not a member of the hive, display an error message and redirect to the hive list page
            messages.error(request, "You are not a member of this hive.")
            return redirect('task_list')

        # Retrieve tasks assigned to the current user in the hive
        assigned_tasks = Task.objects.filter(hive=hive, assignee=request.user)
        # Check if the current user is assigned a task in the hive
        if not assigned_tasks.exists():
            # If the user is not assigned a task in the hive, display an error message and redirect to the hive detail page
            messages.error(request, "You are not assigned a task in this hive.")
            return redirect('hive_detail', hive_id=hive_id)

        # If the user is a member of the hive and assigned a task, proceed with the normal dispatch process
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
<<<<<<< HEAD
        form.instance.hive = get_object_or_404(Hive, id=self.kwargs['hive_id'])
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['assignedTo'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse_lazy('hive_detail', kwargs={'pk': self.kwargs['hive_id']})

    def dispatch(self, request, *args, **kwargs):
        hive = get_object_or_404(Hive, id=self.kwargs['hive_id'])
        if hive.HiveOwner != self.request.user:
            return redirect('dashboard')  # Redirect unauthorized users
        return super().dispatch(request, *args, **kwargs)




    # def dispatch(self, request, *args, **kwargs):
    #     # Retrieve the hive ID from the URL parameters
    #     hive_id = self.kwargs.get('hive_id')
    #     # Retrieve the hive object based on the hive ID
    #     hive = Hive.objects.get(id=hive_id)

    #     # Check if the current user is a member of the hive
    #     membership = Membership.objects.filter(user=request.user, hive=hive).first()
    #     if not membership:
    #             # If the user is not a member of the hive, display an error message and redirect to the hive list page
    #             messages.error(request, "You are not a member of this hive.")
    #             return redirect('hive_list')

    #     if not membership.assigned_tasks:
    #         # If the user is not assigned a task in the hive, display an error message and redirect to the hive detail page
    #         messages.error(request, "You are not assigned a task in this hive.")
    #         return redirect('hive_detail', hive_id=hive_id)

    #     # If the user is a member of the hive and assigned a task, proceed with the normal dispatch process
    #     return super().dispatch(request, *args, **kwargs)


    # def form_valid(self, form):
    #     # Retrieve the hive ID from the URL parameters
    #     hive_id = self.kwargs.get('hive_id')
    #     # Associate the task with the corresponding hive
    #     form.instance.hive = Hive.objects.get(id=hive_id)
    #     return super().form_valid(form)


    # def get_success_url(self):
    #     # Retrieve the hive ID from the URL parameters
    #     hive_id = self.kwargs.get('hive_id')
    #     # Redirect to the hive detail page after successfully creating the task
    #     return reverse_lazy('hive_detail', kwargs={'hive_id': hive_id})
=======
        # Retrieve the hive ID from the URL parameters
        hive_id = self.kwargs.get('hive_id')
        # Associate the task with the corresponding hive
        form.instance.hive = Hive.objects.get(id=hive_id)
        return super().form_valid(form)

    def get_success_url(self):
        # Retrieve the hive ID from the URL parameters
        hive_id = self.kwargs.get('hive_id')
        # Redirect to the hive detail page after successfully creating the task
        return reverse_lazy('hive_detail', kwargs={'hive_id': hive_id})

>>>>>>> parent of 53ac752... task form printing but logic still unperfect



class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'StartDate', 'EndDate']
    template_name = 'hive_manager/update_task.html'
    # context_object_name = 'hives'
    # order = ['-StarDate']

    def form_valid(self, form):
        form.instance.HiveOwner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.assignedTo:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'hive_manager/delete_task.html'
    success_url = reverse_lazy('dashboard')
    # context_object_name = 'hives'
    # order = ['-StarDate']

    # user passes Test to be able to delete task
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.assignedTo:
            return True
        return False



# view membership for CRUD
# code goes here




# @login_required
# def hive_list(request):
#     # Query all hives from the database
#     hives = Hive.objects.all()
#     return render(request, 'hive_manager/hive_list.html', {'hives': hives})

# @login_required
# def hive_detail(request, hive_id):

#         hive = Hive.objects.get(id=hive_id)
#         memberships = Membership.objects.filter(hive=hive)
#         return render(request, 'hive_manager/hive_detail.html', {'hive': hive, 'memberships': memberships})

# @login_required
# def create_hive(request):
#     if request.method == 'POST':
#         form = HiveForm(request.POST)
#         if form.is_valid():
#             hive = form.save(commit=False)
#             hive.queen_bee = request.user
#             hive.save()

#             # Create membership for the Queen Bee
#             Membership.objects.create(User=request.user, hive=hive, role=Membership.QueenBee)
#             return redirect('hive_manager:hive_list')
#     else:
#         form = HiveForm()
#     return render(request, 'hive_manager/create_hive.html', {'form': form})

# @login_required
# def update_hive(request, hive_id):
#     hive = get_object_or_404(Hive, id=hive_id)
#     if request.method == 'POST':
#         form = HiveForm(request.POST, instance=hive)
#         if form.is_valid():
#             form.save()
#             return redirect('hive_manager:hive_detail', hive_id=hive_id)  # Redirect to Hive detail page
#     else:
#         form = HiveForm(instance=hive)
#     return render(request, 'hive_manager/update_hive.html', {'form': form, 'hive': hive})

# @login_required
# def delete_hive(request, hive_id):
#     hive = get_object_or_404(Hive, id=hive_id)
#     if request.method == 'POST':
#         hive.delete()
#         return redirect('hive_manager:hive_list')  # Redirect to Hive list page
#     else:
#         return render(request, 'hive_manager/delete_hive.html', {'hive': hive}) # return redirect('hive_list')


# views for creating task
# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'hive_manager/task_list.html', {'tasks': tasks})

# def task_detail(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     return render(request, 'hive_manager/task_detail.html', {'task': task})

# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hive_manager:task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'hive_manager/create_task.html', {'form': form})

# def update_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('hive_manager:task_list')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'hive_manager/update_task.html', {'form': form})

# def delete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('task_list')
#     return render(request, 'tasks/task_confirm_delete.html', {'task': task})






