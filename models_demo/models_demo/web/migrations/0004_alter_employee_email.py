# Generated by Django 4.1.1 on 2022-10-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
