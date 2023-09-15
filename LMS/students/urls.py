from django.urls import path, include
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import  login, logout
from django.conf.urls.static import static
from django.conf import settings
from .views import index, profile, signup, update, students_login

app_name = "students"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', index, name='students.index'),
    path('login/', students_login, name='students.login'),
    path('signup/', signup.as_view(), name='students.signup'),
    path('profile', profile, name='students.profile'),
    path("<int:id>/update" ,update, name="students.update"),
]