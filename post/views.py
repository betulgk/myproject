from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import post




def home_view(request):
    return render(request, 'home.html', {})


def education_bar(request):
    return render(request, 'education.html', {})

