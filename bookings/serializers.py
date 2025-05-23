from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    tenant = serializers.ReadOnlyField(source='tenant.username')

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'tenant', 'start_date', 'end_date', 'status', 'created_at']
        read_only_fields = ['tenant', 'status', 'created_at']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Дата начала должна быть раньше даты окончания.")
        if data['start_date'] < timezone.now().date():
            raise serializers.ValidationError("Дата начала не может быть в прошлом.")
        return data
