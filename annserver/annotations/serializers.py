from rest_framework import serializers

from annotations.models import Annotation


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['url', 'id', 'owner', 'created', 'data']
