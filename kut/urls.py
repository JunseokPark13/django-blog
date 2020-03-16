from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('problemset/', views.problemset, name='problemset'),
    #path('problem/<pk>', views.problem, name='problem'),
]
