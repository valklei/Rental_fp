import django_filters
from rest_framework.exceptions import ValidationError

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    city = django_filters.CharFilter(field_name="location", lookup_expr='icontains')
    class Meta:
        model = Listing
        fields = ['price_min', 'price_max', 'location']

    def filter_queryset(self, queryset):
        data = self.form.cleaned_data

        price_min = data.get('price_min')
        price_max = data.get('price_max')

        if price_min is not None and price_max is not None:
            if price_min > price_max:
                raise ValidationError("Минимальная цена не может быть больше максимальной.")

        return super().filter_queryset(queryset)