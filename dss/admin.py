from django.contrib import admin
from .models import Course, Course_Comment
from .models import Course_Ratings

# Register your models here.



admin.site.register(Course)
admin.site.register(Course_Ratings)
admin.site.register(Course_Comment)