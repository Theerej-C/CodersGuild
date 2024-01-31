from django.urls import path
from . import views
urlpatterns = [
    path('run_problem/',views.problem_run)
]