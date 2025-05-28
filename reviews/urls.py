from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:listing_id>/', ReviewDetailView.as_view(), name='review-detail'),
]
