from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from listings.models import Listing
from users.models import CustomUser

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'user')  # один отзыв от пользователя на объявление

    def __str__(self):
        return f"Отзыв от {self.user.username} для {self.listing.title}"


# Create your models here.
