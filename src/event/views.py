import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


def index(request):
    list_events = Event.objects.order_by('start_date')[:5]
    list = []
    for data in list_events:
        list.append( {
            'title': data.title,
            'start': str(data.start_date),
            'end': str(data.end_date)
            })
        schedules = data.schedule_set.all()
        print(schedules)
        if schedules:
            for schedule in schedules:
                list.append({
                    'start':f'{schedule.event_date} {schedule.start_time}',
                    'end':f'{schedule.event_date} {schedule.end_time}',
                    'title':schedule.title

                    })
    #print(list)
    return render(request,'index.html',{"list":json.dumps(list)})
