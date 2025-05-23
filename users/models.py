
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('tenant', 'Арендатор'),
        ('landlord', 'Арендодатель'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tenant')

    def __str__(self):
        return f"{self.username} ({self.role})"

