from django.urls import path, include

from expenses_tracker.web.views import index, delete_expense, edit_expense, edit_profile_page,\
    delete_profile_page, profile_page, index_no_profile, create_expense

urlpatterns = (
    path('', index, name='home page'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', include([
        path('', profile_page, name='profile'),
        path('edit/', edit_profile_page, name='edit profile'),
        path('delete/', delete_profile_page, name='delete profile'),
    ])),
)
