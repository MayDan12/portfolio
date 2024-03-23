from django import forms
from .models import Hive

class HiveForm(forms.ModelForm):
    class Meta:
        model = Hive
        fields = ['title', 'description', 'status', 'HiveOwner', 'intendedUsers', 'StartDate', 'EndDate', 'status']

