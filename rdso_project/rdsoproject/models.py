from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Signup(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Employee(models.Model):
    employee = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    address = models.TextField()


