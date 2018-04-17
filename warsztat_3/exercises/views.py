from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from exercises.models import Room, Reservation
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from datetime import datetime, date
import time





def start_page(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        return render(request, "start_page.html", {"rooms": rooms})


def room(request, my_id):
    if request.method == "GET":
        rooms = Room.objects.get(id=my_id)
        return render(request, "room.html", {"rooms": rooms})


@ csrf_exempt
def new_room(request):
    if request.method == "GET":
        return render(request, "new_room.html", {})
    elif request.method == "POST":
        if not request.POST.get("name"):
            return HttpResponse("Please give name")
        if not request.POST.get("seats"):
            return HttpResponse("Please give seats number")
        if request.POST.get("projector"):
            Room.objects.create(name=request.POST.get("name"), seats=request.POST.get("seats"), projector=True)
            return HttpResponse("Dodano salę")
        else:
            Room.objects.create(name=request.POST.get("name"), seats=request.POST.get("seats"), projector=False)
            return HttpResponse("Dodano salę")


def modify_room(request, my_id):
    if request.method == "GET":
        rooms = Room.objects.get(id=my_id)
        return render(request, "modify_room.html", {"rooms": rooms})


def delete_room(request, my_id):
    if request.method == "GET":
        rooms = Room.objects.get(id=my_id)
        return render(request, "delete_room.html", {"rooms": rooms})


def search_room(request):
    pass
    if request.method == "GET":
        # rooms = Room.objects.get(id=my_id)
        return render(request, "search_room.html", {})


@ csrf_exempt
def reserve_room(request, my_id):
    reserve_date = request.POST.get("reserve_date")
    reserve_comment = request.POST.get("reserve_comment")
    if request.method == "GET":
        print(date.today())
        rooms = Room.objects.get(id=my_id)
        return render(request, "reserve_room.html", {"rooms": rooms})
    elif request.method == "POST":
        if not reserve_date:
            return HttpResponse("Please give date")
        # newdate = time.strptime(reserve_date, "%Y-%m-%d")
        today = str(date.today())
        print(today)
        # today_date = time.strptime(today, "%Y-%m-%d")
        if reserve_date < today:
            return HttpResponse("Data nie może być z przeszłości")
        dates = Reservation.objects.filter(date=reserve_date)
        if dates:
            return HttpResponse("Ten termin jest zajęty")
        Reservation.objects.create(room_id=my_id, date=reserve_date, comment=reserve_comment)
        return HttpResponse("Udało się")