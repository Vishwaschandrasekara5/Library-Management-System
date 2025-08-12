from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', context={"current_tab": "home"})

def readers(request):
    return render(request, 'readers.html', context={"current_tab": "readers"})

def books(request):
    return render(request, 'books.html', context={"current_tab": "books"})

def bag(request):
    return render(request, 'bag.html', context={"current_tab": "bag"})

def returns(request):
    return render(request, 'returns.html', context={"current_tab": "returns"})

def shopping(request):
    return HttpResponse("welcome to shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, 'welcome.html', context={'student_name': student_name})