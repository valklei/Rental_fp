from django.urls import path
from users.views import RegisterView, UserDetailView, LogInAPIView, LogOutAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LogInAPIView.as_view(), name='LogInAPIView'),
    path('logout/', LogOutAPIView.as_view(), name='LogOutAPIView'),
]
