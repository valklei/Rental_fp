from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'tenant', 'start_date', 'end_date', 'status', 'created_at')
    #list_display = ('start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('listing__title', 'tenant__username')


# Register your models here.
