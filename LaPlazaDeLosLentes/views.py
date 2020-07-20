#Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, World!, the current server time is: {now}')

def list1(request):
    numbers = [int (i) for i in request.GET['numbers'].split(',')]

    sorted_numbers = sorted(numbers)

    data = {
        'status' : 'ok',
        'data' : sorted_numbers
    }
    #return HttpResponse(json.dumps(data), content_type='application/json')
    return JsonResponse(data, safe=False)
    

def index(request):
    return HttpResponse('hi')