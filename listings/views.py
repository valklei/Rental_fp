from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError

from .filters import ListingFilter
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ListingFilter
    filterset_fields = ['price', 'location', 'room_type', 'rooms_count']
    search_fields = ['location', 'title', 'description']
    ordering_fields = ['price', 'created_at']

    def get_queryset(self):
        try:
            queryset = Listing.objects.filter(is_active=True)
            filterset = self.filterset_class(self.request.GET, queryset=queryset)
            if not filterset.is_valid():
                raise ValidationError(filterset.errors)
            return filterset.qs
        except ValidationError as e:
            raise e

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



# Create your views here.
