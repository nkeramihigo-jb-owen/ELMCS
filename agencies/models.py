from django.conf import settings
from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=200)
    registration_number = models.CharField(
    max_length=100,
    unique=True
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='agencies',
        blank=True
    )

    def __str__(self):
        return self.name

