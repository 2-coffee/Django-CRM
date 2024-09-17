from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Signup_Form,AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records':records})

    

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
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = Signup_Form()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record in records
        customer = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer':customer})
    else:
        messages.success(request,"You Must be Logged In")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"You Must be Logged In")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request,"You Must be Logged In")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request,"You Must be Logged In")
        return redirect('home')