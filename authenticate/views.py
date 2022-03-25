from django.contrib import auth
from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView

from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import user_type, CustomUser


# Create your views here.

def home(request):
    return render(request,'index.html')



    



def shome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request,'index.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return redirect('thome')
    else:
        return redirect('login')
                      
def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return render(request,'index.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('shome')
    else:
        return redirect('home')


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

def signup(request):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    return render(request,'register.html')


def new_home(request):
    return render(request, 'new_home.html')


def signup_teacher(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password==confirm_password:
            if CustomUser.objects.filter(email=email).exists():
                print("error")
            elif CustomUser.objects.filter(username=username).exists():
                print("error")
            else:
                user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                )
                user.set_password(password)
                user.save()
                usert = None     
                usert = user_type(user=user,is_teacher=True)
                usert.save()
                print("user created")
                return redirect('login')
        else:
            print("not created")
            return redirect('signup_teacher')
        
    else:
        return render(request, 'signup_teacher.html')

def signup_student(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = CustomUser.objects.create_user(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()
        usert = None     
        usert = user_type(user=user,is_student=True)
        usert.save()
        print("user created")
        return redirect('login')
        
    else:
        return render(request, 'signup_student.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        type_obj = user_type.objects.get(user=user)
        
        print(type_obj.is_teacher)
       
        if user is not None:
            auth.login(request, user)
            if type_obj.is_teacher:
                return redirect('/teacher_page')
            else:
                return redirect("/")
        else:
            print("error")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



