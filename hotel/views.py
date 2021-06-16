from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from datetime import datetime
from hotel.models import Room, RoomKind


def filter_room(request):
    rk = RoomKind.objects.all()
    return render(request, "hotel/filter.html", {"kinds": rk})


def search_room(request):
    start_date = datetime.strptime(request.GET['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(request.GET['end_date'], "%Y-%m-%d")
    kind = request.GET['kind']
    rooms = Room.objects.filter(
        kind=kind,

    )
    return render(request, "hotel/search.html", {"rooms":rooms})

def hotel_page(request):
    query_set = Room.objects.all()
    context = {"query_set": query_set}
    return render(request, "hotel/index.html", context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {"room": room}
    return render(request, "hotel/room_detail.html", context=context)

def booking_page(request, room_id):
    booking = Room.objects.get(id=room_id)
    context = {"booking": booking}
    return render(request, "hotel/booking_page.html", context=context)



# @login_required()
# @require_http_methods(["POST"])
# def create_booking(request, room_id):
#     text = request.POST["text"]
#     # number = request.POST.get("number_of_seats")
#     date_arrive = request.POST.get["date_arrive"]
#     date_out = request.POST.get["date_out"]
#     Booking.objects.create(
#         text=text,
#         user_id=request.user.id,
#         room_id=room_id,
#         date_arrive=date_arrive,
#         date_out=date_out
#     )
#     return redirect("data_check", room_id=room_id)


@login_required()
def booking_room(request, room_id):
    room = Room.objects.get(id=room_id)
    Booking.objects.create(
        text=request.POST["text"],
        user_id=request.user.id,
        room_id=room_id,
        date_arrive=request.POST.get["date_arrive"],
        date_out=request.POST.get["date_out"]
    )
    room.book_room.add(request.user)
    room.occupation = True
    room.save()
    return redirect("room-detail", room_id=room_id)







