# Generated by Django 4.1.1 on 2022-10-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employee_business_account_employee_job_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='second_email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]