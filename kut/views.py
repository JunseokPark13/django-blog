from django.shortcuts import render
from .models import Problem
# Create your views here.

def main_page(request):
    return render(request, 'koj/index.html', {})

def problemset(request):
    problems = Problem.objects.order_by('prob_id')
    return render(request, 'koj/problemset.html', {'problems': problems})
