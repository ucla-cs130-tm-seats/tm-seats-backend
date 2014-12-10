from ticketmaster.models import User, Seat, Segment

for seat in Seat.objects.all():
  seat.price

for segment in Segment.objects.all()
  segment.placesTotal()
