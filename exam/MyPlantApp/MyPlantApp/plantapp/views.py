from django.shortcuts import render, redirect

from MyPlantApp.plantapp.forms import CreateProfileForm, CreatPlantForm, EditPlantForm, DeletePlantForm, \
    EditProfileForm, DeleteProfileForm
from MyPlantApp.plantapp.models import Profile, Plant


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def plant_catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def creat_plant(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreatPlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant catalogue')
    else:
        form = CreatPlantForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-plant.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    profile = get_profile()

    if request.method == 'POST':
        form = EditPlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant catalogue')

    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'pk': pk,
        'profile': profile,
    }
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    profile = get_profile()

    if request.method == 'POST':
        form = DeletePlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant catalogue')

    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'pk': pk,
        'profile': profile,
    }
    return render(request, 'delete-plant.html', context)


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
        'pk': pk,
    }
    return render(request, 'plant-details.html', context)


def create_profile(request):

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def details_profile(request):
    profile = get_profile()
    total_plant = Plant.objects.count()

    context = {
        'profile': profile,
        'total_plant': total_plant,
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
    }
    return render(request, 'delete-profile.html', context)





