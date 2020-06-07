from django.http import HttpResponse
from django.shortcuts import render
import geocoder
import requests

# Create your views here.

def search_city(request):
    r_json = {}
    if request.POST:
        if request.POST['q']:
            API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/autocomplete/json?"
            query = request.POST.get('q', False)
            print(query)
            params = {
                'input': query,
                'types': "(cities)",
                'key': "AIzaSyAftJH6eF1uB732blxSkmFyA2eYhA5nAPg"
            }
            geo_request = requests.get(API_ENDPOINT, params=params)
            print(geo_request)
            try:
                data = geo_request.json()
                print(data)
            except ValueError:
                print("Response content is not valid JSON")
            return render(request, template_name='city/city_search.html')
        else:
            return HttpResponse("NOK")


