from re import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from authenticate.models import CustomUser
from .models import Course
from django.views.generic import ListView
import json
from django.db.models import Q

from .models import Course_Ratings, Course_Comment

import random



# Create your views here.
def index(request):
    return render(request,'index.html')


def gfqr(request):

    course  = Course.objects.all()
    
    return render(request,'gfqr.html', {'courses':course})

def teacher_page(request):
    return render(request, 'teacher_page.html')

def gfvm(request):
    
    course = Course.objects.all()

    return render(request,'gfvm.html', {'courses':course})

def gt(request):
    
    course = Course.objects.all()

    return render(request,'gt.html', {'courses':course})

def free(request):
    
    course = Course.objects.all()

    return render(request,'free.html', {'courses':course})


def gfhc(request):
    
    course = Course.objects.all()

    return render(request,'gfhc.html', {'courses':course})

def gcap(request):
    
    course = Course.objects.all()

    return render(request,'gcap.html', {'courses':course})


class SearchResultsView(ListView):
    model = Course
    template_name="search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

  

def rate_course(request):
    if request.method == 'POST':
        course_id = int(request.POST.get('course_id'))
        user_id = int(request.POST.get('user_id'))
        val_num = int(request.POST.get('val_num'))
        c_id = Course.objects.get(pk = course_id)
        u_id = CustomUser.objects.get(pk = user_id)
        rating = Course_Ratings(course_id = c_id,user_id = u_id,user_rating = val_num)

        rating.save()
        return JsonResponse({'success':'true'}, safe=False)
    return JsonResponse({'success':'false'})
    

def recommendation(request):
  

    preferences = Course_Ratings.objects.filter(user_rating__gte = 4,user_id = request.user.id)

    
    i = random.randint(0,len(preferences)-1)


    courses = Course.objects.filter(id=preferences[i].course_id_id)
    

    return render(request, "recommendation.html", {"courses" : courses})


def details(request):

    comments = Course_Comment.objects.all()

    return render(request,"details.html",{"comments":comments})


def comment_course(request):
    if request.method == 'POST':
        course_id = int(request.POST.get('course_id'))
        user_id = int(request.POST.get('user_id'))
        comment = request.POST.get('comment')
        c_id = Course.objects.get(pk = course_id)
        u_id = CustomUser.objects.get(pk = user_id)
        comment = Course_Comment(course_id = c_id,user_id = u_id,user_comment = comment)

        comment.save()
        return JsonResponse({'success':'true'}, safe=False)
    return JsonResponse({'success':'false'})



