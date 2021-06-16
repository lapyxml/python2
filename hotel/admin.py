from django.contrib import admin
from hotel.models import Room, RoomKind, BookedRoom

admin.site.register(Room)
admin.site.register(RoomKind)
admin.site.register(BookedRoom)


# Register your models here.
