from django.urls import path

from models_demo.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
