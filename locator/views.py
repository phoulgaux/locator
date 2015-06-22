from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db import IntegrityError
from locator.forms import LocationForm
from locator.models import Location

import requests
import json


def index(request, *args):
    if request.method == 'POST':
        return HttpResponseRedirect('/{}'.format(request.POST['name']))
    vargs = {'form': LocationForm}
    if len(args[0]) > 0:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=' + args[0])
        data = json.loads(response.text)
        message = data['status']
        if data['status'] == 'OK':
            result = Location()
            result.name = data['results'][0]['formatted_address']
            result.latitude = data['results'][0]['geometry']['location']['lat']
            result.longitude = data['results'][0]['geometry']['location']['lng']
            try:
                result.save()
            except IntegrityError:
                pass
        else:
            result = ''
    else:
        message = "Enter a location"
        result = None
    vargs['message'] = message
    vargs['result'] = result
    vargs['history'] = Location.objects.all()
    vargs.update(csrf(request))
    return render_to_response('index.html', vargs)
