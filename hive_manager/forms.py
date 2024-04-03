from django import forms 
from .models import Hive

class CreateHiveForm(forms.ModelForm):
  class Meta():
    model = Hive
    fields = ['title', 'description', 'intendedUsers', 'status', 'StartDate', 'EndDate']

