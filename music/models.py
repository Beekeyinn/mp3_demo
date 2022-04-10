from django.db import models
import os
import random
import string
from django.utils.text import slugify
# Create your models here.


def get_filename_ext(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image_to(instance, filename):
    print("instance", instance)
    print('filename', filename)
    name, ext = get_filename_ext(filename)
    new_name = f"{slugify(name)}-{random.choices(string.ascii_letters+string.digits, k=10)}"
    return f"music/image/{new_name}{ext}"


def upload_audio_to(instance, filename):
    name, ext = get_filename_ext(filename)
    new_name = f"{slugify(name)}-{random.choices(string.ascii_letters+string.digits, k=10)}"
    return f"music/audio/{new_name}{ext}"


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image_to, default=None)
    audio = models.FileField(
        upload_to=upload_audio_to, blank=False, null=False)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name='playlist')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
