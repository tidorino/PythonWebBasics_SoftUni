from django.db import models


class Profile(models.Model):
    pass


class Courses(models.Model):
    image = models.ImageField(
        upload_to='media/',
    )

    summary = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return self.summary

