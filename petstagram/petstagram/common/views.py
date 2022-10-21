from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def apply_user_liked_photo(photo):
    # TODO: fix this for current user when authentication is available
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):
    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):
    user_liked_photo = get_user_liked_photos(photo_id)
    if user_liked_photo:
        user_liked_photo.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')

    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()


def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + reverse('photo details', kwargs={
        'pk': photo_id,
    }))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
