from django.contrib import admin

from MyPlantApp.plantapp.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',)

    def __str__(self):
        return self.username


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
