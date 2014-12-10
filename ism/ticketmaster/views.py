from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from ticketmaster.models import Segment
from ticketmaster.models import Seat
from ticketmaster.models import User
from decimal import Decimal
import json
import requests


# Create your views here.

def geometry(request):
    json_data = open('event-data/0F004CFCCA844D21/0F004CFCCA844D21.geometry.json')
    data = json.load(json_data)
    data_dump = json.dumps(data)
    response = HttpResponse(data_dump, content_type="application/json")
    #response['Content-Disposition'] = 'attachment; filename="geometry.json"'
    return response

def summary(request):
    data = serializers.serialize('json', Segment.objects.all(), fields=('segmentId','placesTotal','placesAvailable'))
    response = HttpResponse(data, content_type="application/json")
    return response

@csrf_exempt
def getSegPrice(request):
    requestId = request.POST["segment"]
    objectQuerySet = Segment.objects.filter(segmentId=requestId).values('price')
    priceOfSeg = int(objectQuerySet[0]['price'])
    return HttpResponse(priceOfSeg)
    #data = serializers.serialize('json', objectQuerySet, fields=('price'))
    #return HttpResponse(data, content_type="application/json")

@csrf_exempt
def filterByPrice(request):
    priceFilter = request.POST["price"]
    objectQuerySet = Segment.objects.filter(price=priceFilter)
    data = serializers.serialize('json', objectQuerySet, fields=('segmentId'))
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def getSegPlace(request):
    requestId = request.POST["segment"]
    json_data = open('event-data/0F004CFCCA844D21/0F004CFCCA844D21.'+requestId+'.places.json')
    data = json.load(json_data)
    data_dump = json.dumps(data)
    response = HttpResponse(data_dump, content_type="application/json")
    return response
    
@csrf_exempt
def reserve(request):
    requestPosition = request.POST["position"]
    splitRequest = requestPosition.split(';',1)
    seatSegment = splitRequest[0]

    isSeatAvail = Seat.objects.filter(position=requestPosition).count()

    if isSeatAvail == 1:
        TotalQuerySet = Segment.objects.filter(segmentId="Total").values('placesAvailable')
        oldTotalPlacesAvail = int(TotalQuerySet[0]['placesAvailable'])
        newTotalPlacesAvail = oldTotalPlacesAvail-1

        Segment.objects.filter(segmentId="Total").update(placesAvailable=newTotalPlacesAvail)

        SegQuerySet = Segment.objects.filter(segmentId=seatSegment).values('placesAvailable')
        oldPlacesAvail = int(SegQuerySet[0]['placesAvailable'])
        newPlacesAvail = oldPlacesAvail-1
    
        Segment.objects.filter(segmentId=seatSegment).update(placesAvailable=newPlacesAvail)

        SeatQuerySet = Seat.objects.filter(position=requestPosition).delete()

        return HttpResponse("Your Seat Has Been Reserved.\nSeat Position: %s\nOld Availability: %d, New Availability: %d\n\nOld Total Availability: %d, New Total Availability: %d" %(requestPosition,oldPlacesAvail,newPlacesAvail,oldTotalPlacesAvail,newTotalPlacesAvail))
    else:
        return HttpResponse("We're sorry. Seat %s is not available." %requestPosition)

@csrf_exempt
def validate(request):
    username = request.POST["username"]
    password = request.POST["password"]
    users = User.objects.filter(user_name="username")
 #   return HttpResponse("0")
    if not users:
      return HttpResponse("2")
    else:
      user = users[0]
      if user.password == password:
        return HttpResponse("0")
      else:
        return HttpResponse("1")
