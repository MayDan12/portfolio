# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     # Add any other fields you want to include in the custom user model

#     def _str_(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    default = 'default.jpg'
    # date_of_birth = models.DateField(blank=True, null=True)
    # Add any other fields you want to include in the user profile

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            display_size = (300, 300)
            img.thumbnail(display_size)
            img.save(self.profile_picture.path)

