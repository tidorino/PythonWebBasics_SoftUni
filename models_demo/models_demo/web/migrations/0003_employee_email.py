# Generated by Django 4.1.1 on 2022-10-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=200, null=True, unique=True),
        ),
    ]
