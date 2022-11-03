from django.db import models
from django.urls.base import reverse

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return self.username


class Record(models.Model):
    voice_record = models.FileField(upload_to="records")
    language = models.CharField(max_length=50, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("recorderApp:record_detail", kwargs={"id": (self.id)})
