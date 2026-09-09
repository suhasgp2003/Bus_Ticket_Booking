
from django.urls import path
from .views import BookingView, RegisterView, LoginView, BusListCreateView, UserBookingsView

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='buslist'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:user_id>/bookings/', UserBookingsView.as_view(), name='user-bookings'),
    path('booking/',BookingView.as_view(),name='bookings')
]