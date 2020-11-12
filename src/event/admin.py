from django.contrib import admin
from .models import Event,Schedule


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 3

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date' , 'end_date']
    inlines = [ScheduleInline]
admin.site.register(Event, EventAdmin)
