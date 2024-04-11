from django import forms
from .models import Hive, Task, Membership

class CreateHiveForm(forms.ModelForm):
  class Meta():
    model = Hive
    fields = ['title', 'description', 'intendedUsers', 'status', 'StartDate', 'EndDate']

class CreateTaskForm(forms.ModelForm):
  def _init_(self, *args, **kwargs):
        hives = kwargs.pop('hives', None)
        super(CreateTaskForm, self)._init_(*args, **kwargs)
        if hives:
            self.fields['hive'].queryset = Hive.objects.filter(id__in=hives)

  class Meta():
    model = Task
    fields = ['hive','title', 'description', 'assignedTo', 'StartDate', 'EndDate']

class MembershipForm(forms.ModelForm):
  class Meta():
    model = Membership
    fields = ['hive', 'user', 'role']
