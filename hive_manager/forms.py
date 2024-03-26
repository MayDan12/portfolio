from django import forms
from .models import Hive, Task

class HiveForm(forms.ModelForm):
    class Meta:
        model = Hive
        fields = ['title', 'description', 'status', 'HiveOwner', 'intendedUsers', 'StartDate', 'EndDate', 'status']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignedTo', 'hive', 'StartDate', 'EndDate']

