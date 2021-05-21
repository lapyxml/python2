from django.urls import path
from hotel import views

urlpatterns = [
    path("room_detail/<int:room_id>/", views.room_detail, name="room-detail"),
    path("", views.hotel_page)
]