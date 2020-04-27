from template.models import Template
from template.serializers import TemplateSerializer
from rest_framework import generics, viewsets


class TemplateList(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
