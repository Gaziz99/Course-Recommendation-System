from django.urls import path

from . import views

# call home function when address is ''

urlpatterns = [
    path('signup_teacher', views.signup_teacher, name='signup_teacher'),
    path('signup_student', views.signup_student, name='signup_student'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    
]