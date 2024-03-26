from django.db import models
from django.contrib.auth.models import User



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

    # Create a model for Task(assigned)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)

    def __str__(self):
                return str(self.id) + " " + self.title

    # Create a model for Membership(members)
class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)
    roleChoices = [
        ('Member', 'Member'),
        ('QueenBee', 'QueenBee'),
        ('Soldier', 'Soldier')
    ]
    # constant BEE
    QueenBee = 'QueenBee'
    role = models.CharField(max_length=20, choices=roleChoices, default=QueenBee)



    def __str__(self):
        return "{} - {} ({})".format(str(self.User.id), str(self.hive), str(self.role))
