from django.db import models
from pathlib import Path
import uuid

# Create your models here.


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.TextField(max_length=2000, verbose_name="Body")
    page_date = models.DateField(verbose_name="Page Date")
    picture = models.ImageField(
        upload_to="diary/picture/", verbose_name="Picture", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)
