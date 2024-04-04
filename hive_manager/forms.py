from django import forms 
from .models import Hive, Task

class CreateHiveForm(forms.ModelForm):
  class Meta():
    model = Hive
    fields = ['title', 'description', 'intendedUsers', 'status', 'StartDate', 'EndDate']
    
class CreateTaskForm(forms.ModelForm):
  class Meta():
    model = Task
    fields = ['title', 'description', 'assignedTo', 'StartDate', 'EndDate']

