from django.contrib import admin
from ticketmaster.models import Segment,Seat

class SeatAdmin(admin.ModelAdmin):
    fields = ['position']
    search_fields = ['position']
admin.site.register(Seat, SeatAdmin)
admin.site.register(Segment)
# Register your models here.
