from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100, unique=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Employee(models.Model):
    employee = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    address = models.TextField()


