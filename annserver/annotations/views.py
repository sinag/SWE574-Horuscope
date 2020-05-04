from annotations.models import Annotation
from annotations.serializers import AnnotationSerializer
from rest_framework import viewsets


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
