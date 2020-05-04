from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from users.serializers import UserSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])  # get the hashed password
        serializer.validated_data['password'] = hashed_password
        user = super(UserViewSet, self).perform_create(serializer)  # create a user

