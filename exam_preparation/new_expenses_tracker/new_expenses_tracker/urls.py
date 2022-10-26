from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('new_expenses_tracker.web.urls')),
] + static(settings.MEDIA_URL,
           documen_root=settings.MEDIA_ROOT,
           )
