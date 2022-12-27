# Generated by Django 4.1.4 on 2022-12-21 07:30

import MyPlantApp.plantapp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantApp.plantapp.validators.validate_first_name_start_with_capital_letter])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantApp.plantapp.validators.validate_first_name_start_with_capital_letter])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]