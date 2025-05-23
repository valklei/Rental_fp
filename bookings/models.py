from django.db import models
from django.utils import timezone
from users.models import CustomUser
from listings.models import Listing

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждено'),
        ('declined', 'Отклонено'),
        ('cancelled', 'Отменено'),
    )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def can_cancel(self):
        from datetime import timedelta
        return timezone.now().date() <= self.start_date - timedelta(days=2)

    def __str__(self):
        return f"Бронирование {self.listing.title} пользователем {self.tenant.username}"


# Create your models here.
