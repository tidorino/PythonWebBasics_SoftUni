from django.urls import path, include

from MyPlantApp.plantapp.views import index, plant_catalogue,\
    creat_plant, edit_plant, delete_plant, details_plant,\
    create_profile, edit_profile, details_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', plant_catalogue, name='plant catalogue'),
    path('create/', creat_plant, name='create plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('profile/', include([
        path('delete/', delete_profile, name='delete profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('create/', create_profile, name='create profile'),
    ])),
)