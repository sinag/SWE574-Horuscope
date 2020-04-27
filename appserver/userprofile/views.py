from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UserPage
from .models import UserProfile


class UserView(View):
    fields = []
    #template_name

    '''def get(self, request):
        string = UserPage.first_name
        print(string)
        html = "<html><body>It is now %s.</body></html>" % string
        return HttpResponse(html)'''

    def get_username(self):
        return UserProfile.userName

    def get_firstname(self):
        return UserProfile.firstName

    def get_datejoined(self):
        return UserProfile.dateJoined

    def get(self,request):
        userName = self.get_username()
        firstName = self.get_firstname()
        dateJoined= self.get_datejoined()

        return render(request,'index.html', {'username': userName, 'firstname' : firstName, 'datejoined':dateJoined})


