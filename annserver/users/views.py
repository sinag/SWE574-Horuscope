from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        serializer.validated_data['password'] = hashed_password
        user = super(UserViewSet, self).perform_create(serializer) # create a user