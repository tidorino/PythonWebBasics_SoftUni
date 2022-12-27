from django.urls import path, include

from CarCollectionApp.web.views import index, car_catalogue, create_car, edit_car, delete_car, details_car, \
    create_profile, details_profile, delete_profile, edit_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', car_catalogue, name='car catalogue'),
    path('car/create/', create_car, name='create car'),
    path('car/', include([
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
        path('<int:pk>/details/', details_car, name='details car'),
    ])),
    path('profile/', include([
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', details_profile, name='details profile'),
        path('create/', create_profile, name='create profile'),
    ])),
)
