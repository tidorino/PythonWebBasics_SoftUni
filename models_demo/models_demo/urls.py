from django.contrib import admin
from django.urls import path, include

import models_demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('models_demo.web.urls')),
]
