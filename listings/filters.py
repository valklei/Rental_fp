import django_filters
from rest_framework.exceptions import ValidationError

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    city = django_filters.CharFilter(field_name="location", lookup_expr='icontains')
    rooms_count = django_filters.NumberFilter(field_name="rooms_count", lookup_expr='gte')
    rooms_count_min = django_filters.NumberFilter(field_name="rooms_count", lookup_expr='gte')
    rooms_count_max = django_filters.NumberFilter(field_name="rooms_count", lookup_expr='lte')

    class Meta:
        model = Listing
        fields = ['price_min', 'price_max', 'city', 'rooms_count', 'rooms_count_min', 'rooms_count_max']

    def filter_queryset(self, queryset):
        data = self.form.cleaned_data

        price_min = data.get('price_min')
        price_max = data.get('price_max')
        rooms_count_min = data.get('rooms_count_min')
        rooms_count_max = data.get('rooms_count_max')

        if rooms_count_min is not None and rooms_count_max is not None:
            if rooms_count_min > rooms_count_max:
                raise ValidationError("Минимальное количество комнат не может быть больше максимального.")

        if price_min is not None and price_max is not None:
            if price_min > price_max:
                raise ValidationError("Минимальная цена не может быть больше максимальной.")

        return super().filter_queryset(queryset)