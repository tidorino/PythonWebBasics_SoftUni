from django.contrib import admin

from CarCollectionApp.web.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age',)

    def __str__(self):
        return self.username


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def __str__(self):
        return self.type | self.model
