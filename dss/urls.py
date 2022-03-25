import imp
from django.urls import path

from . import views

from .views import SearchResultsView

# call home function when address is ''

urlpatterns = [
    path('', views.index, name='index'),
    path('gfqr', views.gfqr, name='gfqr'),
    path('teacher_page', views.teacher_page, name='teacher_page'),
    path('gfvm', views.gfvm, name='gfvm'),
    path('gfhc', views.gfhc, name='gfhc'),
    path('free', views.free, name='free'),
    path('gt', views.gt, name='gt'),
    path('gcap', views.gcap, name='gcap'),
    path('search/', SearchResultsView.as_view(), name="search_results" ),
    path('rate',views.rate_course, name='rate-course'),
    path('recommendation',views.recommendation,name='recommendation'),
    path('details',views.details, name='details'),
    path('comment',views.comment_course, name="comment-course"),
 
]