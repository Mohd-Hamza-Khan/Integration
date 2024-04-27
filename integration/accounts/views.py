from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
import re # import regX module to use search function for special character
from django.contrib import messages
from home.views import home


# password for test user is Harry$$$***000
# Create your views here.
def register(request):
    if request.method=='POST':
        # firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        createpassword = request.POST.get('createpassword')
        confirmpassword = request.POST.get('confirmpassword')
        if createpassword != confirmpassword:
            messages.success(request,"match password with confirm password")
        else:
            lepas = len(createpassword) # length of password
            if lepas < 8: # check password's length
                # print("password should be of 8 digit")
                messages.success(request,f'password should be of 8 digit')
            else:
                if(bool(re.search('^[a-zA-Z0-9]*$',createpassword))==True): # use search function for special character
                    messages.success(request,f"very weak password, \nAdd atleast one special character")  # if special character not found print weak password
                else:
                    messages.success(request,f"strong password") # if special character found print strong password
                    return redirect(home)
        
        
    return render(request, 'register.html')
def index(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, f"logging successfully")
            return redirect('log')

        else:
            # No backend authenticated the credentials
            messages.success(request,"You didn't have an account, Just Sign Up")
            return render(request, 'login.html')

    # messages.success(request,"You didn't have an account, Just Sign Up")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")