# Generated by Django 4.1.3 on 2023-04-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0003_alter_expenses_date_of_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='created_by',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
