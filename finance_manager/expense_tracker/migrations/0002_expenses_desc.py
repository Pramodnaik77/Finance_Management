# Generated by Django 4.1.3 on 2023-04-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='desc',
            field=models.CharField(default=' ', max_length=4000),
        ),
    ]
