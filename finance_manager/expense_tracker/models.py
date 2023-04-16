from django.db import models
from django.contrib.auth.models import User


class expenses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    desc = models.CharField(max_length=4000, default=" ")
    category = models.CharField(max_length=70)
    date_of_expense = models.CharField(max_length=70, default=" ")
    amount = models.CharField(max_length=100, default=" ")
    user_name = models.CharField(max_length=100, default=" ")
    updated_at = models.CharField(max_length=150, default=" ")
    created_by = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return self.name
