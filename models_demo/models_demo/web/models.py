from django.db import models
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=40
    )

    age = models.IntegerField()

    email = models.EmailField(
        unique=True,
        max_length=200,
        # null=True
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'
