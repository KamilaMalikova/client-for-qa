import json
import jsonpickle

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def body_to_dict(body: HttpRequest.body) -> dict or list:
    return json.loads(body)


@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(body_to_dict(request.body.decode('utf-8')))
        # try:
        #
        #     body = body_to_dict(request.body.decode('utf-8'))
        # except json.decoder.JSONDecodeError:
        #     return request, {'ok': False, 'error': 'InvalidBody'}
        # print(**body)
        data = {'ok': True}
        data_json = jsonpickle.encode(data, unpicklable=False)
        return HttpResponse(data_json, content_type='application/json', )
    else:
        data = {'ok': False}
        data_json = jsonpickle.encode(data, unpicklable=False)
        return HttpResponse(data_json, content_type='application/json')
