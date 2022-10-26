from django.urls import path, include

from new_expenses_tracker.web.views import index, create_expense, edit_expense, delete_expense, show_profile, \
    edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', index, name='show index'),
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
