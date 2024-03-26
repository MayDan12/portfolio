from django.contrib import admin
from . models import Hive, Task, Membership, Event

# Register your models here.
admin.site.register(Hive)
admin.site.register(Task)
admin.site.register(Membership)
admin.site.register(Event)
