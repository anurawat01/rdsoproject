from django.shortcuts import render, redirect
from .models import Signup, Employee
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def employee(request):
    return render(request, 'data.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def loginuser(request):
    if request.method == 'POST':
        try:
            usernamex = request.POST['username']
            passwordx = request.POST['password']

            user = authenticate(request, username=usernamex, password=passwordx)
            
            if user is not None:
                login(request, user)
                return redirect('employee-data')  
            else:
                messages.error(request, f'Invalid username or password. {str(usernamex + passwordx)}')
        except Exception as e:
            messages.error(request, f'Error occured during login : {str(e)}')
    
    return render(request, 'login.html')

def signupuser(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm-password']
            # department = request.POST['department']
            # dob = request.POST['dob']
            # phone = request.POST['phone']
            # gender = request.POST['gender']
            
            user = Signup(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
                # department=department,
                # dob=dob,
                # phone=phone,
                # gender=gender
            )

            if Signup.objects.filter(username=username).exists():
                messages.error(request, "Username already registered !")
                return redirect('signup')
            
            if password != confirm_password:
                messages.error(request,"Your password and confirm password are not same!!")
                return redirect('signup')

            user.save()
            messages.success(request, 'You have successfully signed up!')
            return redirect('login')  

        except Exception as e:
            messages.error(request, f'Error occurred during signup: {str(e)}')
    
    return render(request, 'signup.html')

def getEmployeeDetails(request):
    employees = Employee.objects.all()
    print(employees)
    return render(request, 'data.html', {'employees' : employees})
