

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login, logout
from .forms import SignUpForm

from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


def home(request):
    return render(request,"home/home.html")

class RegisterUser(View):
    def get(self, request):
        form=SignUpForm() #da el formulario de registro de django
        return render(request, "autentication/register.html", {"form":form})

    def post(self, request):
        form=SignUpForm(request.POST)

        if form.is_valid():
            user= form.save() #guarda el formulario
            login(request, user)#logea al usuario
            return redirect("Home")

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "autentication/register.html", {"form":form})


def session_out(request):
    logout(request)
    return redirect("Home")


def log(request):
    if request.method=="POST":

        form =AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            name_user= form.cleaned_data.get("username")
            passw_user= form.cleaned_data.get("password")

            user= authenticate(username=name_user, password=passw_user)
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                messages.error(request, "Invalid user")
        
        else:
            messages.error(request, "Incorrect information")
    
    form= AuthenticationForm()
    return render(request, "autentication/logiin.html", {"form":form})



