from django.shortcuts import render, redirect
import mysql.connector as sql
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.http import HttpResponse


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passwd = request.POST.get('password')
        try:
            if "superuser" in name:
                superuser = User.objects.create_superuser(username=name[:-10], password=passwd)
                superuser.save()
                us = authenticate(username=name[:-10], password=passwd)
                login(request, us)
            else:
                u = User.objects.create_user(username=name, password=passwd)
                u.save()
                us = authenticate(username=name, password=passwd)
                login(request, us)
            if us.is_superuser:
                messages.success(request, "Successfully logged in as admin")
            else:
                messages.success(request, "Successfully logged in as Member")
            return redirect("/expense/expense_manager")

        except:
            u = authenticate(username=name, password=passwd)
            if u is not None:
                login(request, u)
                if u.is_superuser:
                    messages.success(request, "Successfully logged in as admin")
                else:
                    messages.success(request, "Successfully logged in as Member")
                return redirect("/expense/expense_manager")
            else:
                messages.error(request, "User Already exist/wrong password")
                return render(request, 'login.html')
    else:
        messages.success(request, "Welcome To Finance Management Application")

    return render(request, 'login.html')
