
from django.db import models
from users.models import CustomUser
from enum import Enum

class RoomType(str, Enum):
    SINGLE_ROOM = "Одна комната (студия)"
    ONE_BEDROOM = "Одна комната с отдельной спальней"
    TWO_BEDROOM = "Две комнаты с общей ванной"
    TWO_BEDROOM_ENSUITE = "Две комнаты с отдельными ванными"
    THREE_BEDROOM = "Три комнаты"
    SUITE = "Сьют / Апартаменты"
    SHARED_ROOM = "Общая комната / койко-место"
    PRIVATE_ROOM_IN_SHARED = "Отдельная комната в общей квартире"
    LOFT = "Лофт / Мансарда"
    STUDIO = "Студия"

    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]

class Listing(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_count = models.PositiveIntegerField()
    room_type = models.CharField(max_length=50, choices=RoomType.choices())
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"


# Create your models here.
