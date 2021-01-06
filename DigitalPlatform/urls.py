from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.show_results, name='show_results'),
    path('solutions/<str:problem>/<int:num_variables>/<str:final>/', views.solution_rest_api, name='solutions_api'),
]
