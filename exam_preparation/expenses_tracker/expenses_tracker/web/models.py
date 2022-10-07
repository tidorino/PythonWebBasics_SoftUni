from django.db import models


class Profile(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    budget = models.FloatField()
    # profile_image = models.ImageField()


class Expense(models.Model):
    title = models.CharField()
    expense_image = models.URLField()
    description = models.TextField()
    price = models.FloatField()
