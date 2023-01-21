from django.urls import path

from MyFinalProject.web.views import show_index

urlpatterns = (
    path('', show_index, name='show index'),
)
