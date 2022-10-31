from django.contrib import admin

from car_collection_app.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
