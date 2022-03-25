from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authenticate.models import CustomUser

# Create your models here.

class Course(models.Model):
   name = models.CharField(max_length=200)
   c_type = models.CharField(max_length=100)
   c_id = models.CharField(max_length=100)
   c_department = models.CharField(max_length=100)
   c_units = models.IntegerField(default=0)
   c_prereq = models.CharField(max_length=200,default="Nil")
   c_content = models.TextField(default='content')
   c_final = models.IntegerField(default=0)
   c_project = models.IntegerField(default=0)
   c_quiz = models.IntegerField(default=0)
   c_assignments = models.IntegerField(default=0)
   c_participation = models.IntegerField(default=0)
   desc = models.TextField(default='course description')
   
   img = models.ImageField()

   class Meta:
      verbose_name_plural = "courses"

   def __str__(self):
       return str(self.name)

class Course_Ratings(models.Model):
   course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
   user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   user_rating = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])

   def __str__(self):
       return self.user_rating

   class Meta:
      ordering = ['user_rating']


class Course_Comment(models.Model):
   course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
   user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   user_comment = models.TextField(default="Comment...")

   def __str__(self):
       return self.user_comment

   class Meta:
      ordering = ['user_comment']