from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from hotel.models import Room



def hotel_page(request):
    query_set = Room.objects.all()
    context = {"query_set": query_set}
    return render(request, "hotel/index.html", context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {"room": room}
    return render(request, "hotel/room_detail.html", context=context)


@login_required()
def booking_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.user in room.book_room.all():
        room.book_room.remove(request.user)
        room.occupation = False
    else:
        room.book_room.add(request.user)
        room.occupation = True
    room.save()
    return redirect("hotel-page")


