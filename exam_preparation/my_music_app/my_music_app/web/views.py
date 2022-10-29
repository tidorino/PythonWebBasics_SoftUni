from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileCreateForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    ProfileDeleteForm
from my_music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

    # try:
    #     return Profile.objects.get()
    # except Profile.DoesNotExist as ex:
    #     return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    albums = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=albums)
    else:
        form = EditAlbumForm(request.POST, request.FILES, instance=albums)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
        'albums': albums,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    albums = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=albums)
    else:
        form = DeleteAlbumForm(request.POST, instance=albums)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
        'albums': albums,
    }
    return render(request, 'delete-album.html', context)


def details_profile(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


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


def create_profile(request):

    if request.method == 'GET':
        form = ProfileCreateForm()

    else:

        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)
