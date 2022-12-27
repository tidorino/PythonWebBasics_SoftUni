from django.shortcuts import render, redirect

from CarCollectionApp.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EdiProfileForm, \
    DeleteProfileForm
from CarCollectionApp.web.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return profiles


def index(request):
    profiles = get_profile()

    cars = Car.objects.all()

    context = {
        'profiles': profiles,
        'cars': cars,
        'no_profile': True,
    }

    return render(request, 'index.html', context)


def car_catalogue(request):
    profiles = get_profile()
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'profiles': profiles,
        'cars': cars,
        'cars_count': cars_count,
    }

    return render(request, 'catalogue.html', context)


def create_car(request):
    profiles = get_profile()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car catalogue')
    else:
        form = CreateCarForm()

    context = {
        'form': form,
        'profiles': profiles,
    }

    return render(request, 'car-create.html', context)


def edit_car(request, pk):
    profiles = get_profile()
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car catalogue')

    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
        'pk': pk,
        'profiles': profiles,
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = DeleteCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car catalogue')

    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
        'pk': pk,
    }

    return render(request, 'car-delete.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
        'pk': pk,
    }

    return render(request, 'car-details.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_car_sum = sum(c.price for c in cars)

    context = {
        'profile': profile,
        'total_car_sum': total_car_sum,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-delete.html', context)


def edit_profile(request):
    profiles = get_profile()

    if request.method == 'POST':
        form = EdiProfileForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    else:
        form = EdiProfileForm(instance=profiles)

    context = {
        'form': form,
        'profiles': profiles,
    }

    return render(request, 'profile-edit.html', context)
