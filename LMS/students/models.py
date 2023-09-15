from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 



class Student(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default=1234)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_students(cls):
        return cls.objects.all()

    @classmethod
    def get_student(cls, id):
        return cls.objects.get(user_id=id)

    def get_profile_url(self):
        return reverse("student.profile", args=[self.id])
    
    def get_edit_url(self):
        return reverse("student.edit", args=[self.id])

