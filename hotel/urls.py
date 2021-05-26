from django.urls import path
from hotel import views

urlpatterns = [
    path("room_detail/<int:room_id>/", views.room_detail, name="room-detail"),
    path("booking_room/<int:room_id>/", views.booking_room, name="booking-room"),
    path("", views.hotel_page, name="hotel-page")
]