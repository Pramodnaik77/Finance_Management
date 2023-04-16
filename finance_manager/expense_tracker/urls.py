from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('expense_manager', views.expense_manager, name="expense_manager"),
    path('create_expense', views.create_expense, name="create_expense"),
    path('edit_expense/<int:myid>', views.edit_expense, name="edit_expense"),
    path('delete_expense/<int:myid>', views.delete_expense, name="delete_expense"),
    path('filter_by_date', views.filter_by_date, name="filter_by_date"),
    path('search_by_name', views.search_by_name, name="search_by_name"),
]
