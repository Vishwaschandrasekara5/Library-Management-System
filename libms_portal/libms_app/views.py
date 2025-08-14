from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import reader  # Import reader model explicitly

# Create your views here.


def home(request):
    return render(request, 'home.html', context={"current_tab": "home"})

def readers(request):
    if request.method == 'GET':
        readers = reader.objects.all()
        return render(request, 'readers.html', context={
            "current_tab": "readers",
            "readers": readers
        })
    else:
        query = request.POST.get('query', '')
        readers = reader.objects.raw(
            "SELECT * FROM libms_app_reader WHERE reader_name LIKE %s", [f"%{query}%"]
        )
        return render(request, 'readers.html', context={
            "current_tab": "readers",
            "readers": readers,
            "query": query
        })

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

def save_reader(request):
    reader_item = reader (reference_id = request.POST['reader_ref_id'],
                            reader_name = request.POST['reader_name'],
                            reader_contact = request.POST['reader_contact'],
                            reader_address = request.POST['reader_address'],
                            active = True)
    reader_item.save()
    return redirect('/readers')
      