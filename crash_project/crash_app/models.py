from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    id = models.BigAutoField(primary_key=True)
    full_name = models.TextField()
    dob = models.DateField()
    email = models.CharField()
    phone = models.CharField(max_length=20, blank=True)
    city = models.TextField()
    institute = models.TextField()
    qualification = models.CharField()
    gender = models.CharField()
    is_active=models.BooleanField(blank=False, null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
