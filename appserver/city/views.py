from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

def search_city(request):

    if request.POST:
        if request.POST['q']:
            API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/autocomplete/json?"
            query = request.POST.get('q', False)
            print(query)
            params = {
                'input': query,
                'length': len(query),
                'types': "(cities)",
                'key': "AIzaSyAftJH6eF1uB732blxSkmFyA2eYhA5nAPg"
            }
            geo_request = requests.get(API_ENDPOINT, params=params)
            try:
                data = geo_request.json()['predictions']
                data = json.dumps(data)
                data = json.loads(data)
                print(data)
            except ValueError:
                print("Response content is not valid JSON")
            return render(request, 'city/city_search.html', {'city_list': data})
        else:
            return render(request, template_name='city/city_search.html')
        return render(request, template_name='city/city_search.html')
    return render(request, template_name='city/city_search.html')


