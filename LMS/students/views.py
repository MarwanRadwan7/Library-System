from django.shortcuts import render,redirect
from students.forms import StudentCreationForm
from students.models import Student 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import  login, logout


def index(request):
    return render(request, "students/index.html")


def profile(request):
    student = Student.get_all_students()
    return render( request, "profile.html", context={'students': student} )

def students_login(request, user):

    login(request, user)
    return redirect('books:books.index')

def update(request, id):
    student = Student.get_student(id = id)
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        student.name = name
        student.phone_number = phone_number
        student.email = email

        student.save()
        user = request.user
        user.username = name
        user.save()
        return redirect("students:students.profile")
        
    return render(request, "update.html" , context={'student':student})

class signup(CreateView):
    model = User
    form_class = StudentCreationForm
    success_url = "/books/all"
    template_name = "signup.html"

    def form_valid(self, form):

        user = form.save()

        student = Student()
        student.name = form.cleaned_data.get('username')
        student.phone_number = form.cleaned_data.get('phone_number')
        student.email = form.cleaned_data.get('email')
        # student.password = user.password
        # student.birthdate = form.cleaned_data.get('birthdate')
        student.user = user
        student.save()

        return super().form_valid(form)
    

def error_404(request, exception):
    return render(request, 'not-found.html')