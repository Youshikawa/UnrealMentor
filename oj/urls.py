from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_problems, name= 'submission'),
    path('results/', views.submission_result, name = "submission_result"),
    path('problems/', views.problem_list, name = 'problem_list'),
    path('problem/',views.problem_details, name="problem_details"),
    path('submission_list/',views.submission_list, name='submission_list')
]