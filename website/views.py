from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Signup_Form

# Create your views here.
def home(request):
    #request is the http link 

    #if request is a POST method
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate from django
        user = authenticate(request, username = username, password = password)

        if user:
            #from django
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"User does not exist")
            return redirect('home')
    return render(request, 'home.html', {})

    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username, password)
            login(request,user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = Signup_Form()
        return render(request, 'register.html', {'form':form})