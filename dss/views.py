from re import template
from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.views.generic import ListView
import json
from django.db.models import Q



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

  