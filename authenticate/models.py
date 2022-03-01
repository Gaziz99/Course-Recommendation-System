from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    def get_email(self):
        return self.email


class user_type(models.Model):
     is_teacher = models.BooleanField(default=False)
     is_student = models.BooleanField(default=False)
     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

     def __str__(self):
         if self.is_student == True:
             return CustomUser.get_email(self.user) + " - is_student"
         else:
             return CustomUser.get_email(self.user) + " - is_teacher"