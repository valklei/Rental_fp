from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'rooms_count', 'room_type', 'owner', 'is_active', 'created_at')
    list_filter = ('room_type', 'location', 'is_active')
    search_fields = ('title', 'description', 'location', 'owner__username')
    readonly_fields = ('created_at',)

# Register your models here.
