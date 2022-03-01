from tabnanny import verbose
from django.db import models

# Create your models here.

class Course(models.Model):
   name = models.CharField(max_length=200)
   c_type = models.CharField(max_length=100)
   desc = models.TextField(default='course description')
   img = models.ImageField()

   class Meta:
      verbose_name_plural = "courses"

   def __str__(self):
       return str(self.name)
