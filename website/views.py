from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    return render(request, 'register.html', {})