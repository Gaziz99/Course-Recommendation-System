from re import template
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from processing import preprocessing
from evaluation import evaluation
from sklearn.metrics.pairwise import linear_kernel

from django_pandas.io import read_frame

from authenticate.models import CustomUser
from .models import Course
from django.views.generic import ListView
import json
from django.db.models import Q

from .models import Course_Ratings, Course_Comment
from django.contrib import messages

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

    course_data = Course.objects.all()
    rating_data = Course_Ratings.objects.all()

    course = read_frame(course_data, fieldnames=['id','name','c_content'])
    rating_data = read_frame(rating_data)

    tfidf = TfidfVectorizer(stop_words='english')
    course['c_content'] = course['c_content'].fillna('')
    overview_matrix = tfidf.fit_transform(course['c_content'])
    similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
    mapping = pd.Series(course.index,index = course['name'])

    preferences = Course_Ratings.objects.filter(user_rating__gte = 3,user_id = request.user.id)
    if not preferences:
        messages.info(request, "Please rate some courses first.")
        return redirect(index)
    else:
        courses = Course.objects.filter(id=preferences[0].course_id_id)

        course_index = mapping[courses[0].name]
        similarity_score = list(enumerate(similarity_matrix[course_index]))
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        similarity_score = similarity_score[1:15]
        course_indices = [i[0] for i in similarity_score]
        recoms = course['name'].iloc[course_indices]

        
        courses =  Course.objects.filter(name__in=recoms)

        
        

        return render(request, "recommendation.html", {"courses" : courses})


def details(request):

    link_url = request.GET.get('q')
    name = link_url.split("|")[12]

  

    comment_objects = Course_Comment.objects.filter(course_id=name)

    user_objects = CustomUser.objects.all()


    return render(request,"details.html",{"comments":comment_objects,"users":user_objects})


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



