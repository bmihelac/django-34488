from django.db import models


class TestModel(models.Model):
    title = models.CharField(
        'title',
        max_length=100,
    )
    document = models.FileField(
        upload_to="documents/",
        verbose_name='document',
        blank=True,
    )
