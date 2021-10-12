from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from Signup_App.forms import *
from django.contrib.auth.decorators import login_required
from Signup_App.models import *


def post(request):
    text = "hajj"
    return HttpResponse(text)


def Home(request):
    return render(request, 'Signup_App/home.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'Signup_App/login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/Signup_App/login/')


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('/Signup_App/home/')
        else:
            messages.info(request, 'password not matching')
            return render(request, "Signup_App/Register.html")
        return redirect('/')
    else:
        return render(request, 'Signup_App/Register.html')
