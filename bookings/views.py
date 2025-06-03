from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'tenant__username']
    #search_fields = ['location', 'title', 'description']
    ordering_fields = ['start_date', 'end_date']

    def get_queryset(self):
        # Пользователь видит только свои бронирования
        return Booking.objects.filter(Q(tenant=self.request.user) | Q(listing__owner=self.request.user))

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user)

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(Q(tenant=self.request.user) | Q(listing__owner=self.request.user))

    def partial_update(self, request, *args, **kwargs):
        # print('patch', '==' * 100)
        instance = self.get_object()
        user = request.user
        data = request.data.copy()
        new_status = data.get('status')
        instance.status = new_status
        instance.save()
        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        print(instance.can_cancel(), '==' * 100)
        if instance.can_cancel():
            instance.delete()
        else:
            raise PermissionDenied("Нельзя отменить бронирование")

# Create your views here.
