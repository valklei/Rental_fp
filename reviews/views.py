from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Review
from .serializers import ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating']
    # search_fields = ['location', 'title', 'description']
    ordering_fields = ['rating']

    def get_queryset(self):
        listing_id = self.request.query_params.get('listing')
        if listing_id:
            return Review.objects.filter(listing_id=listing_id)
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'listing_id'
    lookup_field = 'listing'

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return Review.objects.filter(listing=listing_id)