from django.shortcuts import render
from hotel.models import Room



def hotel_page(request):
    query_set = Room.objects.all()
    context = {"query_set": query_set}
    return render(request, "hotel/index.html", context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {"room": room}
    return render(request, "hotel/room_detail.html", context=context)

