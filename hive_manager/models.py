from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your hive model here.
class Hive(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    intendedUsers = models.IntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    statusChoices = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived')
        ]
    status = models.CharField(max_length=20, choices=statusChoices)
    HiveOwner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # queenBee = models.ForeignKey(QueenBee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.title)

    def get_absolute_url(self):
        return reverse("hive_detail", kwargs={"pk": self.pk})




    # Create a model for Membership(members)
class Membership(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)
    roleChoices = [
        ('Member', 'Member'),
        ('QueenBee', 'QueenBee'),
        ('Soldier', 'Soldier')
    ]
    # constant BEE
    Member = 'Member'
    role = models.CharField(max_length=20, choices=roleChoices, default=Member)


    def __str__(self):
        # return "{} - {} ({})".format(str(self.hive), str(self.role))
        return "{} - {} ({})".format(str(self.hive), str(self.role), str(self.user))

    def get_absolute_url(self):
        return reverse("hive_detail", kwargs={"pk": self.pk})




# Create a model for Task(assigned)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_task')
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)

    def __str__(self):
                return str(self.id) + " " + self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})


# model for events
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

