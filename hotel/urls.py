from django.urls import path
from hotel import views

urlpatterns = [
    path("filter/", views.filter_room, name="filter-room"),
    path("search/", views.search_room, name="search-room"),
    path("room_detail/<int:room_id>/", views.room_detail, name="room-detail"),
    path("booking_room/<int:room_id>/", views.booking_room, name="booking-room"),
    path("booking_page/<int:room_id>/", views.booking_page, name="booking-page"),
    path("", views.hotel_page, name="hotel-page")
]