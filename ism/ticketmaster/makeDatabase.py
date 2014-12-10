import json
from ticketmaster.models import User, Seat, Segment

json_data = open('ticketmaster/event-data/0F004CFCCA844D21/0F004CFCCA844D21.availability.json')
data = json.load(json_data)

if 'availablePlaces' in data:
  availablePlaces = data['availablePlaces']
  for place in availablePlaces:
    seat = Seat.objects.get_or_create(position=place)



json_data = open('ticketmaster/event-data/0F004CFCCA844D21/0F004CFCCA844D21.availabilitySummary.json')
availability_data = json.load(json_data)

totalPlaces = availability_data['placesTotal']
totalPlacesAvailable = availability_data['placesAvailable']
Segment.objects.get_or_create(segmentId='Total', placesTotal = totalPlaces, placesAvailable = totalPlacesAvailable, price=0)

segments = availability_data['segments']
for segment in segments:
  id = segment['segmentId'];
  places = segment['placesTotal'];
  available = segment['placesAvailable'];
  Segment.objects.create(segmentId=id, placesTotal = places, placesAvailable = available, price=0)


json_data = open('ticketmaster/event-data/0F004CFCCA844D21/0F004CFCCA844D21.pricing.json')
pricing_data = json.load(json_data)

if 'prices' in pricing_data:
  prices = pricing_data['prices']
  for price in prices:
    locations = price['places']
    for location in locations:
      loc = str(location)
      seg = loc.rsplit(';',3)[0]
      segments = Segment.objects.filter(segmentId=seg)
      for segment in segments:
        segment.price = price['faceValue']
        segment.save()
