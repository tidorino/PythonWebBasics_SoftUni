from django.urls import path

from my_music_app.web.views import show_index, add_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile, create_profile

urlpatterns = (
    path('', show_index, name='show index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', details_album, name='details album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
