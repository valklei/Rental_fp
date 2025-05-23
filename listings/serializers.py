from rest_framework import serializers
from .models import Listing, RoomType

class ListingSerializer(serializers.ModelSerializer):
    room_type = serializers.ChoiceField(choices=RoomType.choices())

    class Meta:
        model = Listing
        fields = ['id', 'owner', 'title', 'description', 'location', 'price', 'rooms_count', 'room_type', 'is_active', 'created_at']
        read_only_fields = ['owner', 'is_active', 'created_at']

    def create(self, validated_data):
        return Listing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.price = validated_data.get('price', instance.price)
        instance.rooms_count = validated_data.get('rooms_count', instance.rooms_count)
        instance.room_type = validated_data.get('room_type', instance.room_type)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['room_type'] = instance.get_room_type_display()
        return representation

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной")
        return value

    def validate_rooms_count(self, value):
        if value < 0:
            raise serializers.ValidationError("Количество комнат не может быть отрицательным")
        return value

    def validate_location(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Местоположение должно содержать не менее 5 символов")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Описание должно содержать не менее 10 символов")
        return value

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Название должно содержать не менее 5 символов")
        return value

    def validate(self, attrs):
        if attrs['price'] < 0:
            raise serializers.ValidationError({"price": "Цена не может быть отрицательной"})
        if attrs['rooms_count'] < 0:
            raise serializers.ValidationError({"rooms_count": "Количество комнат не может быть отрицательным"})
        if len(attrs['location']) < 5:
            raise serializers.ValidationError({"location": "Местоположение должно содержать не менее 5 символов"})
        if len(attrs['description']) < 10:
            raise serializers.ValidationError({"description": "Описание должно содержать не менее 10 символов"})
        if len(attrs['title']) < 5:
            raise serializers.ValidationError({"title": "Название должно содержать не менее 5 символов"})
        return attrs
    