from django.http import HttpResponse
from django.views import View
from .forms import UserPage


class UserView(View):
    def get(self, request):
        string = UserPage.first_name
        print(string)
        html = "<html><body>It is now %s.</body></html>" % string
        return HttpResponse(html)
