from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Hive, Task, Membership

@receiver(post_save, sender=Hive)
def create_membership(sender, instance, created, **kwargs):
    if created:
        tasks = Task.objects.filter(hive=instance)
        for task in tasks:
            # Assign roles based on task assignments
            role = 'QueenBee' if task.assignedTo == instance.created_by else 'Member' or 'Soldier'
            # Create membership for each user assigned to tasks in the Hive
            Membership.objects.create(user=task.assigned_to, hive=instance, role=role)


