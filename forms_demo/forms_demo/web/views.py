from django import forms
from django.shortcuts import render

from forms_demo.web.models import Person


class NameForm(forms.Form):
    name = forms.CharField(
        max_length=30,
    )


def index(request):
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['name']
        Person.objects.create(
            name=name,
        )

    context = {
        'form': NameForm(),
    }

    return render(request, 'index.html', context)
