from django.http import HttpResponse
from django.shortcuts import render
import geocoder
import requests

# Create your views here.

def search_city(request):
    r_json = {}
    if request.POST:
        if request.POST['q']:
            API_ENDPOINT = "https://api.geonames.org/searchJSON?"
            query = request.POST.get('q', False)
            print(query)

            # params = {
            #     'q': query,
            #     'maxRows':10,
            #     'username':"demo"
            # }
            # geo_request = requests.get(API_ENDPOINT, params=params, verify=False)
            # try:
            #     data = geo_request.json()
            # except ValueError:
            #     print("Response content is not valid JSON")
            g = geocoder.geonames(query, key='horuscope')
            print(g.address)
            return render(request, template_name='city/city_search.html', )
        return HttpResponse("NOK")
    return render(request, template_name='city/city_search.html')
