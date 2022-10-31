from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CreateCarForm, EditCarForm, DeleteCarForm, ProfileDeleteForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def show_catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
        'profile': profile,
        'no_profile': True,
    }

    return render(request, 'profile-create.html', context)


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def details_profile(request):
    profile = get_profile()
    cars_count = Car.objects.count()

    context = {
        'profile': profile,
        'cars_count': cars_count,
    }

    return render(request, 'profile-details.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
    }
    return render(request, 'car-create.html', context)


def edit_car(request, pk):
    cars = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=cars)
    else:
        form = EditCarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
        'cars': cars,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    cars = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=cars)
    else:
        form = DeleteCarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'form': form,
        'cars': cars,
    }

    return render(request, 'car-delete.html', context)


def details_car(request, pk):
    cars = Car.objects.filter(pk=pk).get()

    context = {
        'cars': cars
    }
    return render(request, 'car-details.html', context)
