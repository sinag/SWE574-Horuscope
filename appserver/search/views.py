from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.models import Community


# Create your views here.

def search_basic(request):
    communities = None
    if request.POST:
        community_query = request.POST.get('community_search', False)
        communities = Community.objects.filter(city__icontains=community_query)
        print(communities)
        return render(request, 'search/search_basic.html', {'communities': communities})
    return render(request, 'search/search_basic.html', {'communities': communities})



