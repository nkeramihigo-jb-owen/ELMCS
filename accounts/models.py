from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):


    class Role(models.TextChoices):
        EXPATRIATE = 'EXPATRIATE', 'Expatriate'
        AGENCY = 'AGENCY', 'Agency'
        GOVERNMENT = 'GOVERNMENT', 'Government Officer'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EXPATRIATE
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

