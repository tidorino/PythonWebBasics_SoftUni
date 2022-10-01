from django.urls import path, include

from petstagram.photos.views import add_photo, photo_details, edit_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', photo_details, name='photo details'),
        path('edit/', edit_photo, name='edit photo'),
    ])),
)
