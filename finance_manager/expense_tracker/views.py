from django.shortcuts import render, redirect
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from datetime import datetime
from .models import expenses


# from finance_manager.expense_tracker.models import expenses


def expense_manager(request):
    editable = expenses.objects.filter(user_name=request.user.username)
    non_editable = expenses.objects.exclude(user_name=request.user.username)
    l = 0
    if request.user.is_superuser:
        l = len(non_editable)
    l += len(editable)
    is_exists = False

    if l > 0:
        is_exists = True

    return render(request, 'expense_manager.html',
                  {'editable': editable, 'non_editable': non_editable, 'is_exists': is_exists})


def create_expense(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        category = request.POST.get('cat')
        date_of_expense = request.POST.get('date')
        amount = request.POST.get('expense')
        user_name = request.user.username
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        updated_at = dt_string
        created_by = request.user.username

        finance = expenses(name=name, desc=desc, category=category, date_of_expense=date_of_expense, amount=amount,
                           user_name=user_name, updated_at=updated_at, created_by=created_by)
        finance.save()
        messages.success(request, 'Expense added successfully')
        return redirect('/expense/expense_manager')


def edit_expense(request, myid):
    if request.method == "POST":
        finance = expenses.objects.get(id=myid)
        finance.name = request.POST.get('name' + str(myid), '')
        finance.desc = request.POST.get('desc' + str(myid), '')
        finance.category = request.POST.get('cat' + str(myid))
        finance.date_of_expense = request.POST.get('date' + str(myid))
        finance.amount = request.POST.get('expense' + str(myid))
        finance.user_name = request.user.username
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        finance.updated_at = dt_string

        finance.save()
        messages.success(request, 'Expense edited successfully')
        return redirect('/expense/expense_manager')


def delete_expense(request, myid):
    finance = expenses.objects.get(id=myid)
    finance.delete()
    messages.success(request, 'Expense deleted successfully')
    return redirect('/expense/expense_manager')


def filter_by_date(request):
    if request.method == "POST":
        search_date = request.POST.get('search_date', '')
        editable = expenses.objects.filter(user_name=request.user.username).filter(date_of_expense=search_date)
        non_editable = expenses.objects.exclude(user_name=request.user.username).filter(date_of_expense=search_date)
        is_exists = True
        l = 0
        if request.user.is_superuser:
            l = len(non_editable)
        l += len(editable)

        if l == 0:
            messages.error(request, "No results found")
            return redirect('/expense/expense_manager')
    return render(request, 'expense_manager.html',
                  {'editable': editable, 'non_editable': non_editable, 'is_exists': is_exists})


def search_by_name(request):
    if request.method == "POST":
        search_name = request.POST.get('search_name', '')
        editable = expenses.objects.filter(user_name=request.user.username).filter(name=search_name)
        non_editable = expenses.objects.exclude(user_name=request.user.username).filter(name=search_name)

        is_exists = True
        l = 0
        if request.user.is_superuser:
            l = len(non_editable)
        l += len(editable)

        if l == 0:
            messages.error(request, "No results found")
            return redirect('/expense/expense_manager')
    return render(request, 'expense_manager.html',
                  {'editable': editable, 'non_editable': non_editable, 'is_exists': is_exists})
