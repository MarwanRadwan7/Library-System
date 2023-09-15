from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request

def lms_index(request):
    return render(request, 'index.html')