from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')
