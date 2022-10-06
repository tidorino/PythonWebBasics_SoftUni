# Generated by Django 4.1.1 on 2022-10-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_employee_my_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='EMAIL'),
        ),
    ]
