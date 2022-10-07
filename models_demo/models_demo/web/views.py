from django.contrib.auth.models import User
from django.shortcuts import render

from models_demo.web.models import Employee


def index(request):
    x = list(Employee.objects.all())
    print(User.objects.all())
    print(x)
    pass

