from django.shortcuts import render
import json
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def demo(request):
    jsonStr = {
        'message': 'success',
        'data': {
            'names': [
                {
                    'id': 0,
                    'first_name': 'Jack',
                    'last_name': 'Smith'
                },
                {
                    'id': 1,
                    'first_name': 'Jane',
                    'last_name': 'Zack'
                }
            ]
        }
    }
    response = HttpResponse(json.dumps(jsonStr).encode('utf8'), content_type='application/json;charset=utf-8')
    return response