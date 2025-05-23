from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['location', 'title', 'description']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



# Create your views here.
