from django.contrib import admin
from . models import Hive, Task, Membership

# Register your models here.
admin.site.register(Hive)
admin.site.register(Task)
admin.site.register(Membership)
