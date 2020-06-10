from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
from community.models import Community


def search_city(request, pk):
    community = Community.objects.get(id=pk)
    data = {}
    if request.POST:
        if request.POST['q']:
            API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/autocomplete/json?"
            query = request.POST.get('q', False)
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
            except ValueError:
                print("Response content is not valid JSON")
            return render(request, 'city/city_search.html', {'city_list': data , 'comid' : pk, 'community':community})
        elif request.POST['selectq']:
            selectq = request.POST.get('selectq')
            print(selectq)
            community.city = selectq;
            community.save()
            return redirect('community:posts', pk)
        return render(request, 'city/city_search.html', {'city_list': data, 'comid' : pk, 'community':community})
    return render(request, 'city/city_search.html', {'comid': pk, 'community':community})

#, 'comid' : pk