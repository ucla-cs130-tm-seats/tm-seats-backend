import json
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from ticketmaster.models import User, Seat
# Create your views here.

def index(request):
  users_list = User.objects.order_by('user_name')[:5]
  context = {'users_list': users_list}
  return render(request, 'ticketmaster/index.html', context)

def detail(request, username):
  return HttpResponse("You're looking at %s." % username)

def login(request):
   return render(request, 'ticketmaster/login.html')

def validate(request):
   username = request.POST['username']
   password = request.POST['password']
   users = User.objects.filter(user_name=username)
   if not users:   
     return render(request, 'ticketmaster/detail.html',
     {'text': 'Username not valid',
     })
   else:
     user = users[0]
     if user.password == password:
       return render(request, 'ticketmaster/detail.html',
       {'text': 'Login successful',
       })
     else:
       return render(request, 'ticketmaster/detail.html',
       {'text': 'Password incorrect',
       })

def readJsonFilesIntoDatabase():
  json_data = open('event-data/0F004CFCCA844D21/0F004CFCCA844D21.availability.json')
  data = json.load(json.data)

  if 'availablePlaces' in data:
    availablePlaces = data['availablePlaces']
    for place in availableSeats:
      seat = Seat.objects.create(position=place)
