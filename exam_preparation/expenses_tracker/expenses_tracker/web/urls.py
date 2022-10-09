from django.urls import path, include

from expenses_tracker.web.views import show_index, delete_expense, edit_expense, edit_profile,\
    delete_profile, show_profile, create_profile, create_expense

urlpatterns = (
    path('', show_index, name='show index'),

    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),

    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('create/', create_profile, name='create profile'),
    ])),
)
